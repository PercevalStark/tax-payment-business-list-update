import csv
import json
from datetime import datetime, timezone, timedelta
from pytz import timezone
from google.cloud import datastore

from utils import read_from_json_file


taxes_to_remove = read_from_json_file("results/taxes_to_remove.json")
utilities_to_remove = read_from_json_file("results/utilities_to_remove.json")

taxes_code_segment = {(t['code'], t['segment']) for t in taxes_to_remove}
utilities_code_segment = {(u['code'], u['segment']) for u in utilities_to_remove}

# print(taxes_code_segment)
# print(utilities_code_segment)

class DatastoreClient:
    _client = None

    def __init__(self, projectId):
        self._client = datastore.Client(projectId)

    def query(self, kind, filters=None, order=None, page_size=200, cursor=None):
        filters = filters or []
        query = self._client.query(kind=kind)

        for filter in filters:
            query.add_filter(*filter)

        if order:
            query.order = order

        iterator = query.fetch(limit=page_size, start_cursor=cursor)
        if iterator:
            results = list(iterator)
            for result in results:
                result["id"] = result.key.id
                result["contentIn"] = result.get("contentIn", "") or ""
                result["contentOut"] = result.get("contentOut", "") or ""

            return results, iterator.next_page_token

        return [], None

    def delete(self, keys):
        for key in keys:
            self._client.delete(key)

    def key(self, kind, value):
        return self._client.key(kind, value)


if __name__ == "__main__":
    tz = timezone("America/Sao_Paulo")
    filtered_results = []

    client = DatastoreClient("api-ms-tax-payment")
    ref_datetime = datetime.now(tz=tz)
    filters = [("created", ">", datetime.now(tz=tz) - timedelta(days=60))]
    order = ["created"]


    results, cursor = client.query(kind="BarCodePayment", filters=filters, order=order, page_size=10000)
    offset = len(results)
    print(offset)
    while cursor:
        for result in results:
            barcode = result["barCode"]
            code = barcode[1]
            segment = barcode[15:19].lstrip("0") or "0"

            if (code, segment) in taxes_code_segment or (code, segment) in utilities_code_segment:
                filtered_results.append({"code": code, "segment": segment, **result})

        results, cursor = client.query(kind="BarCodePayment", filters=filters, order=order, page_size=40000, cursor=cursor)
        offset += len(results)
        print(cursor, offset, len(filtered_results))

    print(len(filtered_results))

    if not filtered_results:
        quit()

    with open('results/recent_payments_to_verify.csv', "w") as csvfile:
        fieldnames = filtered_results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(filtered_results)
