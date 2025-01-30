from enum import Enum


class BarCodeType(Enum):

    utility = "utility"
    das = "das"
    iss = "iss"
    darf = "darf"
    gps = "gps"
    fgts = "fgts"
    gnre = "gnre"
    dare = "dare"
    dae = "dae"

taxes = [
    {
        "code": "5701",
        "segment": "1",
        "name": "Prefeitura de São Paulo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "0",
        "segment": "1",
        "name": "Prefeitura de São Paulo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3011",
        "segment": "1",
        "name": "Prefeitura de Osasco",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "511",
        "segment": "1",
        "name": "Prefeitura de Belém",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4639",
        "segment": "1",
        "name": "Prefeitura de Uberlândia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1",
        "segment": "1",
        "name": "Prefeitura de Abadia Dourados",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2",
        "segment": "1",
        "name": "Prefeitura de Abadiania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3",
        "segment": "1",
        "name": "Prefeitura de Abaete",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4",
        "segment": "1",
        "name": "Prefeitura de Abaetetuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "12",
        "segment": "1",
        "name": "Prefeitura de Abreu E Lima",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "26",
        "segment": "1",
        "name": "Prefeitura de Acucena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "60",
        "segment": "1",
        "name": "Prefeitura de Aguas Da Prata",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "62",
        "segment": "1",
        "name": "Prefeitura de Aguas Lindoia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "69",
        "segment": "1",
        "name": "Prefeitura de Agudos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "73",
        "segment": "1",
        "name": "Prefeitura de Aimores",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "84",
        "segment": "1",
        "name": "Prefeitura de Alagoinhas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "99",
        "segment": "1",
        "name": "Prefeitura de Alexania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "100",
        "segment": "1",
        "name": "Prefeitura de Alfenas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "113",
        "segment": "1",
        "name": "Prefeitura de A Tamandare",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "117",
        "segment": "1",
        "name": "Prefeitura de Alpinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "125",
        "segment": "1",
        "name": "Prefeitura de Alterosa Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "131",
        "segment": "1",
        "name": "Prefeitura de Alto Araguaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "137",
        "segment": "1",
        "name": "Prefeitura de Alto Paraiso",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "141",
        "segment": "1",
        "name": "Prefeitura de Alto R Doce",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "145",
        "segment": "1",
        "name": "Prefeitura de Altonia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "154",
        "segment": "1",
        "name": "Prefeitura de Alvinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "155",
        "segment": "1",
        "name": "Prefeitura de Alvorada",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "193",
        "segment": "1",
        "name": "Prefeitura de Ananindeua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "194",
        "segment": "1",
        "name": "Prefeitura de Anapolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "203",
        "segment": "1",
        "name": "Prefeitura de Andradas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "206",
        "segment": "1",
        "name": "Prefeitura de Andrelandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "215",
        "segment": "1",
        "name": "Prefeitura de Angra Dos Reis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "220",
        "segment": "1",
        "name": "Prefeitura de Anicuns",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "227",
        "segment": "1",
        "name": "Prefeitura de Antonina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "243",
        "segment": "1",
        "name": "Prefeitura de Ap Goiania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "259",
        "segment": "1",
        "name": "Prefeitura de Aquidauana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "262",
        "segment": "1",
        "name": "Prefeitura de Aracai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "263",
        "segment": "1",
        "name": "Prefeitura de Aracaju",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "264",
        "segment": "1",
        "name": "Prefeitura de Aracariguama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "273",
        "segment": "1",
        "name": "Prefeitura de Aracruz",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "276",
        "segment": "1",
        "name": "Prefeitura de Aragarcas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "298",
        "segment": "1",
        "name": "Prefeitura de Araponga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "305",
        "segment": "1",
        "name": "Prefeitura de Ararangua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "306",
        "segment": "1",
        "name": "Prefeitura de Araraquara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "311",
        "segment": "1",
        "name": "Prefeitura de Araruama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "313",
        "segment": "1",
        "name": "Prefeitura de Araruna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "319",
        "segment": "1",
        "name": "Prefeitura de Araucaria",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "321",
        "segment": "1",
        "name": "Prefeitura de Araxa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "323",
        "segment": "1",
        "name": "Prefeitura de Arcos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "324",
        "segment": "1",
        "name": "Prefeitura de Arcoverde",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "340",
        "segment": "1",
        "name": "Prefeitura de Ariquemes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "347",
        "segment": "1",
        "name": "Prefeitura de Arraial Cabo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "356",
        "segment": "1",
        "name": "Prefeitura de Aruana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "357",
        "segment": "1",
        "name": "Prefeitura de Aruja",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "363",
        "segment": "1",
        "name": "Prefeitura de Assis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "365",
        "segment": "1",
        "name": "Prefeitura de A. Chateaubrian",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "375",
        "segment": "1",
        "name": "Prefeitura de Atibaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "385",
        "segment": "1",
        "name": "Prefeitura de Aurilandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "393",
        "segment": "1",
        "name": "Prefeitura de Avare",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "419",
        "segment": "1",
        "name": "Prefeitura de Balsa Nova",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "433",
        "segment": "1",
        "name": "Prefeitura de B Cocais",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "440",
        "segment": "1",
        "name": "Prefeitura de Barbacena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "447",
        "segment": "1",
        "name": "Prefeitura de Bariri",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "449",
        "segment": "1",
        "name": "Prefeitura de Barra Bonita",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "462",
        "segment": "1",
        "name": "Prefeitura de Barra Do Garcas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "471",
        "segment": "1",
        "name": "Prefeitura de Barra Mansa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "473",
        "segment": "1",
        "name": "Prefeitura de Barracao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "482",
        "segment": "1",
        "name": "Prefeitura de Barretos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "485",
        "segment": "1",
        "name": "Prefeitura de Barro Alto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "493",
        "segment": "1",
        "name": "Prefeitura de Barroso",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "502",
        "segment": "1",
        "name": "Prefeitura de Bauru",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "504",
        "segment": "1",
        "name": "Prefeitura de Bebedouro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "508",
        "segment": "1",
        "name": "Prefeitura de Bela Vista Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "509",
        "segment": "1",
        "name": "Prefeitura de Bela Vista Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "521",
        "segment": "1",
        "name": "Prefeitura de B.Horizonte",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "539",
        "segment": "1",
        "name": "Prefeitura de Bertioga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "545",
        "segment": "1",
        "name": "Prefeitura de Betim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "548",
        "segment": "1",
        "name": "Prefeitura de Bicas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "553",
        "segment": "1",
        "name": "Prefeitura de Biritiba Mirim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "556",
        "segment": "1",
        "name": "Prefeitura de Bituruna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "559",
        "segment": "1",
        "name": "Prefeitura de Boa Esperanca",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "567",
        "segment": "1",
        "name": "Prefeitura de Boa Vista",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "569",
        "segment": "1",
        "name": "Prefeitura de Boa Vista Apareci",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "583",
        "segment": "1",
        "name": "Prefeitura de Boituva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "585",
        "segment": "1",
        "name": "Prefeitura de Bom Despacho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "598",
        "segment": "1",
        "name": "Prefeitura de Bom Jesus",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "601",
        "segment": "1",
        "name": "Prefeitura de Bom Jesus Galho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "607",
        "segment": "1",
        "name": "Prefeitura de Bom Jesus Perdoes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "617",
        "segment": "1",
        "name": "Prefeitura de Bonfim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "635",
        "segment": "1",
        "name": "Prefeitura de Boraceia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "643",
        "segment": "1",
        "name": "Prefeitura de Botelhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "644",
        "segment": "1",
        "name": "Prefeitura de Botucatu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "651",
        "segment": "1",
        "name": "Prefeitura de Braganca Pta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "675",
        "segment": "1",
        "name": "Prefeitura de Brazopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "695",
        "segment": "1",
        "name": "Prefeitura de Brumadinho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "696",
        "segment": "1",
        "name": "Prefeitura de Brumado Ba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "698",
        "segment": "1",
        "name": "Prefeitura de Bueno Brandao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "723",
        "segment": "1",
        "name": "Prefeitura de Cabeceiras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "729",
        "segment": "1",
        "name": "Prefeitura de Cabo Frio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "732",
        "segment": "1",
        "name": "Prefeitura de Cabreuva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "736",
        "segment": "1",
        "name": "Prefeitura de Cacapava",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "746",
        "segment": "1",
        "name": "Prefeitura de Cach Pajeu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "753",
        "segment": "1",
        "name": "Prefeitura de Cachoeiras Macacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "765",
        "segment": "1",
        "name": "Prefeitura de Cacoal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "772",
        "segment": "1",
        "name": "Prefeitura de Caete",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "778",
        "segment": "1",
        "name": "Prefeitura de Cafelandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "782",
        "segment": "1",
        "name": "Prefeitura de Caiaponia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "789",
        "segment": "1",
        "name": "Prefeitura de Caieiras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "793",
        "segment": "1",
        "name": "Prefeitura de Cajamar",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "810",
        "segment": "1",
        "name": "Prefeitura de Caldas Novas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "813",
        "segment": "1",
        "name": "Prefeitura de California",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "816",
        "segment": "1",
        "name": "Prefeitura de Camacari",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "823",
        "segment": "1",
        "name": "Prefeitura de Camaragibe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "830",
        "segment": "1",
        "name": "Prefeitura de Camboriu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "831",
        "segment": "1",
        "name": "Prefeitura de Cambuci",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "837",
        "segment": "1",
        "name": "Prefeitura de Campanario",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "838",
        "segment": "1",
        "name": "Prefeitura de Campanha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "839",
        "segment": "1",
        "name": "Prefeitura de Campestre",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "846",
        "segment": "1",
        "name": "Prefeitura de Campina Verde",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "849",
        "segment": "1",
        "name": "Prefeitura de Campinas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "858",
        "segment": "1",
        "name": "Prefeitura de Campo Belo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "866",
        "segment": "1",
        "name": "Prefeitura de Campo Florido",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "868",
        "segment": "1",
        "name": "Prefeitura de Cpo Grande Ms",
        "time": "20H",
        "type": BarCodeType.iss,
    },
    {
        "code": "870",
        "segment": "1",
        "name": "Prefeitura de Campo Largo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "871",
        "segment": "1",
        "name": "Prefeitura de Cpo Limpo Pta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "876",
        "segment": "1",
        "name": "Prefeitura de Cpo Novo Parecis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "879",
        "segment": "1",
        "name": "Prefeitura de Campos Altos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "882",
        "segment": "1",
        "name": "Prefeitura de Campos Jordao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "883",
        "segment": "1",
        "name": "Prefeitura de Cpos Goytacazes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "897",
        "segment": "1",
        "name": "Prefeitura de Canapolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "903",
        "segment": "1",
        "name": "Prefeitura de Candeias",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "915",
        "segment": "1",
        "name": "Prefeitura de Canela",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "927",
        "segment": "1",
        "name": "Prefeitura de Cantagalo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "935",
        "segment": "1",
        "name": "Prefeitura de Capanema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "957",
        "segment": "1",
        "name": "Prefeitura de Capitolio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "958",
        "segment": "1",
        "name": "Prefeitura de Capivari",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "967",
        "segment": "1",
        "name": "Prefeitura de Carambei",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "969",
        "segment": "1",
        "name": "Prefeitura de Carandai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "970",
        "segment": "1",
        "name": "Prefeitura de Carangola",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "971",
        "segment": "1",
        "name": "Prefeitura de Carapicuiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "972",
        "segment": "1",
        "name": "Prefeitura de Caratinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "977",
        "segment": "1",
        "name": "Prefeitura de Carazinho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "981",
        "segment": "1",
        "name": "Prefeitura de Cardos Moreira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "982",
        "segment": "1",
        "name": "Prefeitura de Careacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "985",
        "segment": "1",
        "name": "Prefeitura de Cariacica",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "999",
        "segment": "1",
        "name": "Prefeitura de Carmo Cachoeira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1000",
        "segment": "1",
        "name": "Prefeitura de Carmo Mata",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1003",
        "segment": "1",
        "name": "Prefeitura de Carmo Paranaiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1004",
        "segment": "1",
        "name": "Prefeitura de Carmo Rio Claro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1017",
        "segment": "1",
        "name": "Prefeitura de Carrancas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1022",
        "segment": "1",
        "name": "Prefeitura de Carvalhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1032",
        "segment": "1",
        "name": "Prefeitura de Casimiro Abreu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1034",
        "segment": "1",
        "name": "Prefeitura de Cassia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1037",
        "segment": "1",
        "name": "Prefeitura de Castanhal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1040",
        "segment": "1",
        "name": "Prefeitura de Castelo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1043",
        "segment": "1",
        "name": "Prefeitura de Castro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1045",
        "segment": "1",
        "name": "Prefeitura de Cataguases",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1046",
        "segment": "1",
        "name": "Prefeitura de Catalao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1051",
        "segment": "1",
        "name": "Prefeitura de C Altas Noruega",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1061",
        "segment": "1",
        "name": "Prefeitura de Caucaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1063",
        "segment": "1",
        "name": "Prefeitura de Caxambu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1066",
        "segment": "1",
        "name": "Prefeitura de Caxias Do Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1076",
        "segment": "1",
        "name": "Prefeitura de Centenario Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1083",
        "segment": "1",
        "name": "Prefeitura de Cerquilho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1091",
        "segment": "1",
        "name": "Prefeitura de Ceu Azul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1092",
        "segment": "1",
        "name": "Prefeitura de Cezarina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1121",
        "segment": "1",
        "name": "Prefeitura de Claraval",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1124",
        "segment": "1",
        "name": "Prefeitura de Claudio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1150",
        "segment": "1",
        "name": "Prefeitura de Colorado",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1153",
        "segment": "1",
        "name": "Prefeitura de Coluna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1163",
        "segment": "1",
        "name": "Prefeitura de Conceicao Alagoas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1166",
        "segment": "1",
        "name": "Prefeitura de Conceicao Macabu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1174",
        "segment": "1",
        "name": "Prefeitura de Conceicao Para",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1178",
        "segment": "1",
        "name": "Prefeitura de Conchal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1189",
        "segment": "1",
        "name": "Prefeitura de Congonhal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1190",
        "segment": "1",
        "name": "Prefeitura de Congonhas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1193",
        "segment": "1",
        "name": "Prefeitura de Conquista",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1194",
        "segment": "1",
        "name": "Prefeitura de Cons Lafaiete",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1196",
        "segment": "1",
        "name": "Prefeitura de Conselheiro Pena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1199",
        "segment": "1",
        "name": "Prefeitura de Contagem",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1200",
        "segment": "1",
        "name": "Prefeitura de Contenda",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1202",
        "segment": "1",
        "name": "Prefeitura de Coqueiral",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1208",
        "segment": "1",
        "name": "Prefeitura de Cordeiropolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1211",
        "segment": "1",
        "name": "Prefeitura de Cordislandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1216",
        "segment": "1",
        "name": "Prefeitura de Corinto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1221",
        "segment": "1",
        "name": "Prefeitura de Coromandel",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1224",
        "segment": "1",
        "name": "Prefeitura de C Fabriciano",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1237",
        "segment": "1",
        "name": "Prefeitura de Corrego Bom Jesus",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1246",
        "segment": "1",
        "name": "Prefeitura de Corumba Goias",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1247",
        "segment": "1",
        "name": "Prefeitura de Corumbaiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1253",
        "segment": "1",
        "name": "Prefeitura de Cosmopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1258",
        "segment": "1",
        "name": "Prefeitura de Cotia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1277",
        "segment": "1",
        "name": "Prefeitura de Cristalina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1278",
        "segment": "1",
        "name": "Prefeitura de Cristiano Otoni",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1294",
        "segment": "1",
        "name": "Prefeitura de Cruzeiro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1295",
        "segment": "1",
        "name": "Prefeitura de Cruzeiro Fortalez",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1299",
        "segment": "1",
        "name": "Prefeitura de Cruzeiro Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1319",
        "segment": "1",
        "name": "Prefeitura de Curitiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1321",
        "segment": "1",
        "name": "Prefeitura de Curiuva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1330",
        "segment": "1",
        "name": "Prefeitura de Curvelo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1333",
        "segment": "1",
        "name": "Prefeitura de Damolandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1339",
        "segment": "1",
        "name": "Prefeitura de Delfim Moreira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1340",
        "segment": "1",
        "name": "Prefeitura de Delfinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1346",
        "segment": "1",
        "name": "Prefeitura de Descalvado",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1350",
        "segment": "1",
        "name": "Prefeitura de Dest Entre Rios",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1359",
        "segment": "1",
        "name": "Prefeitura de Diamantina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1362",
        "segment": "1",
        "name": "Prefeitura de Dias D Avila",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1376",
        "segment": "1",
        "name": "Prefeitura de Divinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1387",
        "segment": "1",
        "name": "Prefeitura de Dois Vizinhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1391",
        "segment": "1",
        "name": "Prefeitura de Dom Cavati",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1406",
        "segment": "1",
        "name": "Prefeitura de Dona Euzebia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1426",
        "segment": "1",
        "name": "Prefeitura de Dracena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1433",
        "segment": "1",
        "name": "Prefeitura de Duque Caxias",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1447",
        "segment": "1",
        "name": "Prefeitura de Eloi Mendes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1450",
        "segment": "1",
        "name": "Prefeitura de Embu Das Artes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1460",
        "segment": "1",
        "name": "Prefeitura de Eng Beltrao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1463",
        "segment": "1",
        "name": "Prefeitura de Eng Navarro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1464",
        "segment": "1",
        "name": "Prefeitura de Eng Paulo Frontin",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1466",
        "segment": "1",
        "name": "Prefeitura de Entre Rios Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1484",
        "segment": "1",
        "name": "Prefeitura de Esmeraldas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1495",
        "segment": "1",
        "name": "Prefeitura de Espirito Sto Pinh",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1496",
        "segment": "1",
        "name": "Prefeitura de Esp Santo Do Turv",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1504",
        "segment": "1",
        "name": "Prefeitura de Estiva Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1505",
        "segment": "1",
        "name": "Prefeitura de Estiva Gerbi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1517",
        "segment": "1",
        "name": "Prefeitura de Eugenopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1519",
        "segment": "1",
        "name": "Prefeitura de Eusebio Ce",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1521",
        "segment": "1",
        "name": "Prefeitura de Extrema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1529",
        "segment": "1",
        "name": "Prefeitura de Fama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1544",
        "segment": "1",
        "name": "Prefeitura de Fazenda Rio Grand",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1547",
        "segment": "1",
        "name": "Prefeitura de Feira Santana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1562",
        "segment": "1",
        "name": "Prefeitura de Ferraz Vasconcelo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1584",
        "segment": "1",
        "name": "Prefeitura de Floresta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1587",
        "segment": "1",
        "name": "Prefeitura de Florestopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1597",
        "segment": "1",
        "name": "Prefeitura de Formosa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1600",
        "segment": "1",
        "name": "Prefeitura de Formoso",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1605",
        "segment": "1",
        "name": "Prefeitura de Fortaleza",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1612",
        "segment": "1",
        "name": "Prefeitura de Foz Iguacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1619",
        "segment": "1",
        "name": "Prefeitura de Francisco Beltrao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1636",
        "segment": "1",
        "name": "Prefeitura de Frutal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1649",
        "segment": "1",
        "name": "Prefeitura de Garanhuns",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1656",
        "segment": "1",
        "name": "Prefeitura de Gaspar",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1682",
        "segment": "1",
        "name": "Prefeitura de Goianesia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1685",
        "segment": "1",
        "name": "Prefeitura de Goianira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1689",
        "segment": "1",
        "name": "Prefeitura de Goiatuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1703",
        "segment": "1",
        "name": "Prefeitura de Gov Valadares",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1737",
        "segment": "1",
        "name": "Prefeitura de Guanhaes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1738",
        "segment": "1",
        "name": "Prefeitura de Guape",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1742",
        "segment": "1",
        "name": "Prefeitura de Guapo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1750",
        "segment": "1",
        "name": "Prefeitura de Guaraciaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1762",
        "segment": "1",
        "name": "Prefeitura de Guaraniacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1767",
        "segment": "1",
        "name": "Prefeitura de Guaraquecaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1780",
        "segment": "1",
        "name": "Prefeitura de Guaruja",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1782",
        "segment": "1",
        "name": "Prefeitura de Guarulhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1784",
        "segment": "1",
        "name": "Prefeitura de Guaxupe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1791",
        "segment": "1",
        "name": "Prefeitura de Gurinhata",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1804",
        "segment": "1",
        "name": "Prefeitura de Hidrolandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1806",
        "segment": "1",
        "name": "Prefeitura de Holambra",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1810",
        "segment": "1",
        "name": "Prefeitura de Hortolandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1832",
        "segment": "1",
        "name": "Prefeitura de Ibia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1851",
        "segment": "1",
        "name": "Prefeitura de Ibiraiaras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1859",
        "segment": "1",
        "name": "Prefeitura de Ibirite Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1862",
        "segment": "1",
        "name": "Prefeitura de Ibitinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1868",
        "segment": "1",
        "name": "Prefeitura de Ibiuna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1882",
        "segment": "1",
        "name": "Prefeitura de Igaracu Tiete",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1884",
        "segment": "1",
        "name": "Prefeitura de Igarape",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1899",
        "segment": "1",
        "name": "Prefeitura de Iguatemi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1902",
        "segment": "1",
        "name": "Prefeitura de Ijaci",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1903",
        "segment": "1",
        "name": "Prefeitura de Ijui",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1909",
        "segment": "1",
        "name": "Prefeitura de Ilicinea",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1923",
        "segment": "1",
        "name": "Prefeitura de Inconfidentes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1924",
        "segment": "1",
        "name": "Prefeitura de Indaial",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1925",
        "segment": "1",
        "name": "Prefeitura de Indaiatuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1941",
        "segment": "1",
        "name": "Prefeitura de Inhapim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1945",
        "segment": "1",
        "name": "Prefeitura de Inhumas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1949",
        "segment": "1",
        "name": "Prefeitura de Ipameri",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1950",
        "segment": "1",
        "name": "Prefeitura de Ipanema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1953",
        "segment": "1",
        "name": "Prefeitura de Ipatinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1954",
        "segment": "1",
        "name": "Prefeitura de Ipaussu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1964",
        "segment": "1",
        "name": "Prefeitura de Ipiranga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1968",
        "segment": "1",
        "name": "Prefeitura de Ipojuca",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1969",
        "segment": "1",
        "name": "Prefeitura de Ipora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1970",
        "segment": "1",
        "name": "Prefeitura de Ipora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1983",
        "segment": "1",
        "name": "Prefeitura de Iracemapolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1995",
        "segment": "1",
        "name": "Prefeitura de Irati",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1997",
        "segment": "1",
        "name": "Prefeitura de Irece",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2012",
        "segment": "1",
        "name": "Prefeitura de Itabira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2014",
        "segment": "1",
        "name": "Prefeitura de Itabirito",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2015",
        "segment": "1",
        "name": "Prefeitura de Itaborai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2016",
        "segment": "1",
        "name": "Prefeitura de Itabuna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2030",
        "segment": "1",
        "name": "Prefeitura de Itaguai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2031",
        "segment": "1",
        "name": "Prefeitura de Itaguaje",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2041",
        "segment": "1",
        "name": "Prefeitura de Itaipe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2046",
        "segment": "1",
        "name": "Prefeitura de Itaju Tributos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2048",
        "segment": "1",
        "name": "Prefeitura de Itajuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2050",
        "segment": "1",
        "name": "Prefeitura de Italva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2062",
        "segment": "1",
        "name": "Prefeitura de Itambe Mato Dentr",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2063",
        "segment": "1",
        "name": "Prefeitura de Itamogi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2066",
        "segment": "1",
        "name": "Prefeitura de Itanhaem",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2069",
        "segment": "1",
        "name": "Prefeitura de Itanhomi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2072",
        "segment": "1",
        "name": "Prefeitura de Itaocara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2073",
        "segment": "1",
        "name": "Prefeitura de Itapaci",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2079",
        "segment": "1",
        "name": "Prefeitura de Itapecerica",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2080",
        "segment": "1",
        "name": "Prefeitura de Itapecerica Serra",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2085",
        "segment": "1",
        "name": "Prefeitura de Itaperuna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2087",
        "segment": "1",
        "name": "Prefeitura de Itapetinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2090",
        "segment": "1",
        "name": "Prefeitura de Itapeva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2091",
        "segment": "1",
        "name": "Prefeitura de Itapevi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2094",
        "segment": "1",
        "name": "Prefeitura de Itapira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2103",
        "segment": "1",
        "name": "Prefeitura de Itapolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2110",
        "segment": "1",
        "name": "Prefeitura de Itapui",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2113",
        "segment": "1",
        "name": "Prefeitura de Itaquaquecetuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2120",
        "segment": "1",
        "name": "Prefeitura de Itarare",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2122",
        "segment": "1",
        "name": "Prefeitura de Itariri Sp",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2124",
        "segment": "1",
        "name": "Prefeitura de Itatiaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2126",
        "segment": "1",
        "name": "Prefeitura de Itatiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2133",
        "segment": "1",
        "name": "Prefeitura de Itau De Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2135",
        "segment": "1",
        "name": "Prefeitura de Itaucu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2137",
        "segment": "1",
        "name": "Prefeitura de Itauna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2148",
        "segment": "1",
        "name": "Prefeitura de Itu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2151",
        "segment": "1",
        "name": "Prefeitura de Itueta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2152",
        "segment": "1",
        "name": "Prefeitura de Ituiutaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2153",
        "segment": "1",
        "name": "Prefeitura de Itumbiara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2154",
        "segment": "1",
        "name": "Prefeitura de Itumirim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2158",
        "segment": "1",
        "name": "Prefeitura de Iturama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2160",
        "segment": "1",
        "name": "Prefeitura de Ituverava",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2167",
        "segment": "1",
        "name": "Prefeitura de Ivinhema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2171",
        "segment": "1",
        "name": "Prefeitura de Jaboatao Guararap",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2178",
        "segment": "1",
        "name": "Prefeitura de Jaboticatubas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2190",
        "segment": "1",
        "name": "Prefeitura de Jacobina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2197",
        "segment": "1",
        "name": "Prefeitura de Jacutinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2198",
        "segment": "1",
        "name": "Prefeitura de Jaguapita",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2210",
        "segment": "1",
        "name": "Prefeitura de Jaguariuna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2216",
        "segment": "1",
        "name": "Prefeitura de Jambeiro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2217",
        "segment": "1",
        "name": "Prefeitura de Janauba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2237",
        "segment": "1",
        "name": "Prefeitura de Jaragua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2249",
        "segment": "1",
        "name": "Prefeitura de Jarinu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2251",
        "segment": "1",
        "name": "Prefeitura de Jatai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2256",
        "segment": "1",
        "name": "Prefeitura de Jau",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2260",
        "segment": "1",
        "name": "Prefeitura de Jeceaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2262",
        "segment": "1",
        "name": "Prefeitura de Jequie",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2265",
        "segment": "1",
        "name": "Prefeitura de Jequitinhonha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2272",
        "segment": "1",
        "name": "Prefeitura de Jesuitas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2273",
        "segment": "1",
        "name": "Prefeitura de Ji-Parana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2279",
        "segment": "1",
        "name": "Prefeitura de Joanopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2285",
        "segment": "1",
        "name": "Prefeitura de Joao Monlevade",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2288",
        "segment": "1",
        "name": "Prefeitura de Joao Pinheiro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2294",
        "segment": "1",
        "name": "Prefeitura de Joaquim Tavora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2303",
        "segment": "1",
        "name": "Prefeitura de Joviania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2314",
        "segment": "1",
        "name": "Prefeitura de Juiz De Fora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2319",
        "segment": "1",
        "name": "Prefeitura de Jundiai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2337",
        "segment": "1",
        "name": "Prefeitura de Jussara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2352",
        "segment": "1",
        "name": "Prefeitura de Lages",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2378",
        "segment": "1",
        "name": "Prefeitura de Lagoa Santa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2385",
        "segment": "1",
        "name": "Prefeitura de Laje Muriae",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2392",
        "segment": "1",
        "name": "Prefeitura de Lajinha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2394",
        "segment": "1",
        "name": "Prefeitura de Lambari",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2403",
        "segment": "1",
        "name": "Prefeitura de Laranjal Pta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2405",
        "segment": "1",
        "name": "Prefeitura de Laranjeiras Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2409",
        "segment": "1",
        "name": "Prefeitura de Lauro De Freitas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2412",
        "segment": "1",
        "name": "Prefeitura de Lavras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2418",
        "segment": "1",
        "name": "Prefeitura de Leme",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2420",
        "segment": "1",
        "name": "Prefeitura de Lencois Pta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2422",
        "segment": "1",
        "name": "Prefeitura de Leopoldina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2431",
        "segment": "1",
        "name": "Prefeitura de Limeira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2437",
        "segment": "1",
        "name": "Prefeitura de Lindoia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2447",
        "segment": "1",
        "name": "Prefeitura de Londrina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2470",
        "segment": "1",
        "name": "Prefeitura de Luz",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2471",
        "segment": "1",
        "name": "Prefeitura de Luziania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2473",
        "segment": "1",
        "name": "Prefeitura de Macae",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2477",
        "segment": "1",
        "name": "Prefeitura de Macapa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2480",
        "segment": "1",
        "name": "Prefeitura de Macatuba Tributos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2485",
        "segment": "1",
        "name": "Prefeitura de Maceio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2486",
        "segment": "1",
        "name": "Prefeitura de Machacalis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2489",
        "segment": "1",
        "name": "Prefeitura de Machado",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2502",
        "segment": "1",
        "name": "Prefeitura de Mage",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2506",
        "segment": "1",
        "name": "Prefeitura de Mairipora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2516",
        "segment": "1",
        "name": "Prefeitura de Mallet",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2524",
        "segment": "1",
        "name": "Prefeitura de Manaus",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2531",
        "segment": "1",
        "name": "Prefeitura de Mangaratiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2533",
        "segment": "1",
        "name": "Prefeitura de Manhuacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2543",
        "segment": "1",
        "name": "Prefeitura de Mar De Espanha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2551",
        "segment": "1",
        "name": "Prefeitura de Maracaju",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2573",
        "segment": "1",
        "name": "Prefeitura de Mal C.Rondon",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2581",
        "segment": "1",
        "name": "Prefeitura de Mariana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2592",
        "segment": "1",
        "name": "Prefeitura de Marilia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2593",
        "segment": "1",
        "name": "Prefeitura de Mariluz",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2594",
        "segment": "1",
        "name": "Prefeitura de Maringa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2619",
        "segment": "1",
        "name": "Prefeitura de Matao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2622",
        "segment": "1",
        "name": "Prefeitura de Matelandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2624",
        "segment": "1",
        "name": "Prefeitura de Mateus Leme",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2625",
        "segment": "1",
        "name": "Prefeitura de Mathias Lobato",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2638",
        "segment": "1",
        "name": "Prefeitura de Matozinhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2647",
        "segment": "1",
        "name": "Prefeitura de Maurilandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2655",
        "segment": "1",
        "name": "Prefeitura de Medianeira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2660",
        "segment": "1",
        "name": "Prefeitura de Mendes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2661",
        "segment": "1",
        "name": "Prefeitura de Mendes Pimentel",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2664",
        "segment": "1",
        "name": "Prefeitura de Meridiano",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2679",
        "segment": "1",
        "name": "Prefeitura de Minacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2683",
        "segment": "1",
        "name": "Prefeitura de Mineiros",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2689",
        "segment": "1",
        "name": "Prefeitura de Miracema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2714",
        "segment": "1",
        "name": "Prefeitura de Mococa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2717",
        "segment": "1",
        "name": "Prefeitura de Moema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2719",
        "segment": "1",
        "name": "Prefeitura de Mogi Das Cruzes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2720",
        "segment": "1",
        "name": "Prefeitura de Mogi Guacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2721",
        "segment": "1",
        "name": "Prefeitura de Mogi Mirim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2730",
        "segment": "1",
        "name": "Prefeitura de Mongagua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2744",
        "segment": "1",
        "name": "Prefeitura de Monte Alegre Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2749",
        "segment": "1",
        "name": "Prefeitura de Monte Aprazivel",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2753",
        "segment": "1",
        "name": "Prefeitura de Mte Carmelo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2759",
        "segment": "1",
        "name": "Prefeitura de Monte Mor",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2762",
        "segment": "1",
        "name": "Prefeitura de Monte Sto Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2763",
        "segment": "1",
        "name": "Prefeitura de Monte Siao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2767",
        "segment": "1",
        "name": "Prefeitura de Montenegro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2769",
        "segment": "1",
        "name": "Prefeitura de Mtes Claros",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2771",
        "segment": "1",
        "name": "Prefeitura de Montividiu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2779",
        "segment": "1",
        "name": "Prefeitura de Morretes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2793",
        "segment": "1",
        "name": "Prefeitura de Mossamedes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2819",
        "segment": "1",
        "name": "Prefeitura de Muriae Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2826",
        "segment": "1",
        "name": "Prefeitura de Mutum",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2828",
        "segment": "1",
        "name": "Prefeitura de Muzambinho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2834",
        "segment": "1",
        "name": "Prefeitura de Natercia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2835",
        "segment": "1",
        "name": "Prefeitura de Natividade",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2840",
        "segment": "1",
        "name": "Prefeitura de Navirai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2846",
        "segment": "1",
        "name": "Prefeitura de Nazareno",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2849",
        "segment": "1",
        "name": "Prefeitura de Nazario",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2851",
        "segment": "1",
        "name": "Prefeitura de Nepomuceno",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2852",
        "segment": "1",
        "name": "Prefeitura de Neropolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2857",
        "segment": "1",
        "name": "Prefeitura de Nilopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2861",
        "segment": "1",
        "name": "Prefeitura de Niquelandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2863",
        "segment": "1",
        "name": "Prefeitura de Niteroi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2875",
        "segment": "1",
        "name": "Prefeitura de N Sra Socorro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2894",
        "segment": "1",
        "name": "Prefeitura de Nova Crixas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2905",
        "segment": "1",
        "name": "Prefeitura de Nova Friburgo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2911",
        "segment": "1",
        "name": "Prefeitura de Nova Iguacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2917",
        "segment": "1",
        "name": "Prefeitura de Nova Lima",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2922",
        "segment": "1",
        "name": "Prefeitura de Nova Odessa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2923",
        "segment": "1",
        "name": "Prefeitura de Nova Olimpia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2934",
        "segment": "1",
        "name": "Prefeitura de Nova Prata Iguacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2943",
        "segment": "1",
        "name": "Prefeitura de Nova Serrana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2952",
        "segment": "1",
        "name": "Prefeitura de Nova Veneza",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2995",
        "segment": "1",
        "name": "Prefeitura de Oliveira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3014",
        "segment": "1",
        "name": "Prefeitura de Osvaldo Cruz",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3020",
        "segment": "1",
        "name": "Prefeitura de Ourinhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3023",
        "segment": "1",
        "name": "Prefeitura de Ouro Branco",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3026",
        "segment": "1",
        "name": "Prefeitura de Ouro Fino",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3027",
        "segment": "1",
        "name": "Prefeitura de Ouro Preto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3034",
        "segment": "1",
        "name": "Prefeitura de Ourolandia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3059",
        "segment": "1",
        "name": "Prefeitura de Palma",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3066",
        "segment": "1",
        "name": "Prefeitura de Palmas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3083",
        "segment": "1",
        "name": "Prefeitura de Palminopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3098",
        "segment": "1",
        "name": "Prefeitura de Para De Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3099",
        "segment": "1",
        "name": "Prefeitura de Paracambi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3100",
        "segment": "1",
        "name": "Prefeitura de Paracatu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3102",
        "segment": "1",
        "name": "Prefeitura de Paragominas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3103",
        "segment": "1",
        "name": "Prefeitura de Paraguacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3104",
        "segment": "1",
        "name": "Prefeitura de Paraguacu Pta",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3106",
        "segment": "1",
        "name": "Prefeitura de Paraiba Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3108",
        "segment": "1",
        "name": "Prefeitura de Paraibuna",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3114",
        "segment": "1",
        "name": "Prefeitura de Paraisopolis Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3121",
        "segment": "1",
        "name": "Prefeitura de Paranagua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3123",
        "segment": "1",
        "name": "Prefeitura de Paranaiguara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3132",
        "segment": "1",
        "name": "Prefeitura de Paraopeba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3133",
        "segment": "1",
        "name": "Prefeitura de Parapua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3134",
        "segment": "1",
        "name": "Prefeitura de Paraty",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3137",
        "segment": "1",
        "name": "Prefeitura de Parauapebas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3143",
        "segment": "1",
        "name": "Prefeitura de Parintins",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3154",
        "segment": "1",
        "name": "Prefeitura de Passa Quatro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3165",
        "segment": "1",
        "name": "Prefeitura de Passos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3167",
        "segment": "1",
        "name": "Prefeitura de Paty Do Alferes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3171",
        "segment": "1",
        "name": "Prefeitura de Patos De Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3173",
        "segment": "1",
        "name": "Prefeitura de Patrocinio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3182",
        "segment": "1",
        "name": "Prefeitura de Paula Candido",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3185",
        "segment": "1",
        "name": "Prefeitura de Paulinia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3187",
        "segment": "1",
        "name": "Prefeitura de Paulista Pe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3203",
        "segment": "1",
        "name": "Prefeitura de Pederneiras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3205",
        "segment": "1",
        "name": "Prefeitura de Pedra Azul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3224",
        "segment": "1",
        "name": "Prefeitura de Pedreira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3236",
        "segment": "1",
        "name": "Prefeitura de Pedro Leopoldo Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3248",
        "segment": "1",
        "name": "Prefeitura de Penapolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3256",
        "segment": "1",
        "name": "Prefeitura de Perdigao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3258",
        "segment": "1",
        "name": "Prefeitura de Perdoes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3266",
        "segment": "1",
        "name": "Prefeitura de Peruibe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3271",
        "segment": "1",
        "name": "Prefeitura de Petrolina Pe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3272",
        "segment": "1",
        "name": "Prefeitura de Petrolina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3273",
        "segment": "1",
        "name": "Prefeitura de Petropolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3282",
        "segment": "1",
        "name": "Prefeitura de Piedade",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3285",
        "segment": "1",
        "name": "Prefeitura de Piedade Gerais",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3286",
        "segment": "1",
        "name": "Prefeitura de Pien",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3309",
        "segment": "1",
        "name": "Prefeitura de Pinhalao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3312",
        "segment": "1",
        "name": "Prefeitura de Pinhao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3324",
        "segment": "1",
        "name": "Prefeitura de Piracaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3325",
        "segment": "1",
        "name": "Prefeitura de Piracanjuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3326",
        "segment": "1",
        "name": "Prefeitura de Piracema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3327",
        "segment": "1",
        "name": "Prefeitura de Piracicaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3329",
        "segment": "1",
        "name": "Prefeitura de Pirai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3331",
        "segment": "1",
        "name": "Prefeitura de Pirai Do Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3332",
        "segment": "1",
        "name": "Prefeitura de Piraju",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3333",
        "segment": "1",
        "name": "Prefeitura de Pirajuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3338",
        "segment": "1",
        "name": "Prefeitura de Pirangucu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3339",
        "segment": "1",
        "name": "Prefeitura de Piranguinho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3340",
        "segment": "1",
        "name": "Prefeitura de Piranhas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3345",
        "segment": "1",
        "name": "Prefeitura de Pirapora",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3348",
        "segment": "1",
        "name": "Prefeitura de Piraquara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3350",
        "segment": "1",
        "name": "Prefeitura de Pirassununga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3355",
        "segment": "1",
        "name": "Prefeitura de Pirenopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3356",
        "segment": "1",
        "name": "Prefeitura de Pires Do Rio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3362",
        "segment": "1",
        "name": "Prefeitura de Pitanga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3363",
        "segment": "1",
        "name": "Prefeitura de Pitangueiras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3389",
        "segment": "1",
        "name": "Prefeitura de Poco Fundo Ipt",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3394",
        "segment": "1",
        "name": "Prefeitura de Pocos Caldas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3395",
        "segment": "1",
        "name": "Prefeitura de Pocrane",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3405",
        "segment": "1",
        "name": "Prefeitura de Ponta Grossa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3407",
        "segment": "1",
        "name": "Prefeitura de Pontal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3409",
        "segment": "1",
        "name": "Prefeitura de Pontalina Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3415",
        "segment": "1",
        "name": "Prefeitura de Ponte Nova",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3423",
        "segment": "1",
        "name": "Prefeitura de Porangatu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3424",
        "segment": "1",
        "name": "Prefeitura de Porciuncula",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3433",
        "segment": "1",
        "name": "Prefeitura de Porto Alegre",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3437",
        "segment": "1",
        "name": "Prefeitura de P.Amazonas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3459",
        "segment": "1",
        "name": "Prefeitura de Posse",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3466",
        "segment": "1",
        "name": "Prefeitura de Pouso Alegre",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3475",
        "segment": "1",
        "name": "Prefeitura de Praia Grande",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3481",
        "segment": "1",
        "name": "Prefeitura de Prata",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3491",
        "segment": "1",
        "name": "Prefeitura de Pres Epitacio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3504",
        "segment": "1",
        "name": "Prefeitura de Pres Prudente",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3508",
        "segment": "1",
        "name": "Prefeitura de Pres Venceslau",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3516",
        "segment": "1",
        "name": "Prefeitura de Promissao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3526",
        "segment": "1",
        "name": "Prefeitura de Quartel Geral",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3529",
        "segment": "1",
        "name": "Prefeitura de Quatis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3532",
        "segment": "1",
        "name": "Prefeitura de Quedas Do Iguacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3536",
        "segment": "1",
        "name": "Prefeitura de Queimados",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3543",
        "segment": "1",
        "name": "Prefeitura de Quintas Do Sol",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3547",
        "segment": "1",
        "name": "Prefeitura de Quirinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3549",
        "segment": "1",
        "name": "Prefeitura de Quitandinha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3561",
        "segment": "1",
        "name": "Prefeitura de Rancharia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3566",
        "segment": "1",
        "name": "Prefeitura de Raul Soares",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3569",
        "segment": "1",
        "name": "Prefeitura de Recife",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3570",
        "segment": "1",
        "name": "Prefeitura de Recreio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3587",
        "segment": "1",
        "name": "Prefeitura de Resende",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3589",
        "segment": "1",
        "name": "Prefeitura de Reserva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3591",
        "segment": "1",
        "name": "Prefeitura de Resplendor",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3627",
        "segment": "1",
        "name": "Prefeitura de Ribeirao Neves",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3629",
        "segment": "1",
        "name": "Prefeitura de Ribeirao Pinhal",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3632",
        "segment": "1",
        "name": "Prefeitura de Ribeirao Pires",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3634",
        "segment": "1",
        "name": "Prefeitura de Ribeirao Vermelho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3640",
        "segment": "1",
        "name": "Prefeitura de Rio Acima",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3641",
        "segment": "1",
        "name": "Prefeitura de Rio Azul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3646",
        "segment": "1",
        "name": "Prefeitura de Rio Branco",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3652",
        "segment": "1",
        "name": "Prefeitura de Rio Claro Rj",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3653",
        "segment": "1",
        "name": "Prefeitura de Rio Claro Sp",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3656",
        "segment": "1",
        "name": "Prefeitura de Rio Das Flores",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3686",
        "segment": "1",
        "name": "Prefeitura de Rio Pomba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3689",
        "segment": "1",
        "name": "Prefeitura de Rio Quente",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3693",
        "segment": "1",
        "name": "Prefeitura de Rio Verde",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3710",
        "segment": "1",
        "name": "Prefeitura de Rolim De Moura",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3713",
        "segment": "1",
        "name": "Prefeitura de Roncador",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3738",
        "segment": "1",
        "name": "Prefeitura de Sabara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3745",
        "segment": "1",
        "name": "Prefeitura de Sacramento",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3767",
        "segment": "1",
        "name": "Prefeitura de Salto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3771",
        "segment": "1",
        "name": "Prefeitura de Salto Itarare",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3776",
        "segment": "1",
        "name": "Prefeitura de Salvador",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3790",
        "segment": "1",
        "name": "Prefeitura de Sta Barbara",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3792",
        "segment": "1",
        "name": "Prefeitura de Sta Barbara/Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3809",
        "segment": "1",
        "name": "Prefeitura de S Cruz Capibaribe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3824",
        "segment": "1",
        "name": "Prefeitura de Sta Gertrudes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3827",
        "segment": "1",
        "name": "Prefeitura de Sta Helena Pr",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3828",
        "segment": "1",
        "name": "Prefeitura de S Helena Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3833",
        "segment": "1",
        "name": "Prefeitura de Sta Isabel",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3846",
        "segment": "1",
        "name": "Prefeitura de Sta Luzia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3867",
        "segment": "1",
        "name": "Prefeitura de S Maria Madalena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3868",
        "segment": "1",
        "name": "Prefeitura de Sta Mariana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3883",
        "segment": "1",
        "name": "Prefeitura de Sta Rita Passa Qu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3884",
        "segment": "1",
        "name": "Prefeitura de S Rita Sapucai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3908",
        "segment": "1",
        "name": "Prefeitura de Santana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3912",
        "segment": "1",
        "name": "Prefeitura de S Cataguases",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3937",
        "segment": "1",
        "name": "Prefeitura de Santo Amaro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3941",
        "segment": "1",
        "name": "Prefeitura de Santo Andre-D",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3943",
        "segment": "1",
        "name": "Prefeitura de Sto Angelo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3951",
        "segment": "1",
        "name": "Prefeitura de Sto Antonio Jesus",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3953",
        "segment": "1",
        "name": "Prefeitura de Sto Antonio Padua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3955",
        "segment": "1",
        "name": "Prefeitura de S Antonio Amparo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3969",
        "segment": "1",
        "name": "Prefeitura de Sto Ant Sudoeste",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3981",
        "segment": "1",
        "name": "Prefeitura de Stos Dumont",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3995",
        "segment": "1",
        "name": "Prefeitura de S Bernardo Campo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4001",
        "segment": "1",
        "name": "Prefeitura de S Bras Do Suacui",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4003",
        "segment": "1",
        "name": "Prefeitura de S Caetano Sul",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4007",
        "segment": "1",
        "name": "Prefeitura de Sao Carlos Ivai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4032",
        "segment": "1",
        "name": "Prefeitura de S Fco Goias",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4048",
        "segment": "1",
        "name": "Prefeitura de Sao Geraldo Mg",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4051",
        "segment": "1",
        "name": "Prefeitura de Sao Goncalo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4053",
        "segment": "1",
        "name": "Prefeitura de S Goncalo Amarant",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4056",
        "segment": "1",
        "name": "Prefeitura de Sao Goncalo Para",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4070",
        "segment": "1",
        "name": "Prefeitura de S Joao Alianca",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4077",
        "segment": "1",
        "name": "Prefeitura de Sao Joao Da Ponte",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4084",
        "segment": "1",
        "name": "Prefeitura de S J Meriti",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4086",
        "segment": "1",
        "name": "Prefeitura de S Joao Del Rei",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4102",
        "segment": "1",
        "name": "Prefeitura de S Joao Evangelist",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4108",
        "segment": "1",
        "name": "Prefeitura de S Jorge Oeste",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4110",
        "segment": "1",
        "name": "Prefeitura de S Jorg Patrocinio",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4128",
        "segment": "1",
        "name": "Prefeitura de S Jose Alegre",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4137",
        "segment": "1",
        "name": "Prefeitura de Sao Jose Divino",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4145",
        "segment": "1",
        "name": "Prefeitura de S Jose Jacuri",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4157",
        "segment": "1",
        "name": "Prefeitura de S J Vale R Preto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4158",
        "segment": "1",
        "name": "Prefeitura de Sjcampos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4160",
        "segment": "1",
        "name": "Prefeitura de S Jose Pinhais",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4165",
        "segment": "1",
        "name": "Prefeitura de S Lourenco-Trib",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4171",
        "segment": "1",
        "name": "Prefeitura de Sao Luis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4172",
        "segment": "1",
        "name": "Prefeitura de Montes Belos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4186",
        "segment": "1",
        "name": "Prefeitura de S Mates Es",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4215",
        "segment": "1",
        "name": "Prefeitura de S Pedro Aldeia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4229",
        "segment": "1",
        "name": "Prefeitura de Sao Roque",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4231",
        "segment": "1",
        "name": "Prefeitura de S Sebastiao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4237",
        "segment": "1",
        "name": "Prefeitura de S Sebastiao Alto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4251",
        "segment": "1",
        "name": "Prefeitura de S Simao Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4256",
        "segment": "1",
        "name": "Prefeitura de S Tome Das Letras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4261",
        "segment": "1",
        "name": "Prefeitura de Sao Vicente",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4269",
        "segment": "1",
        "name": "Prefeitura de Sapopema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4271",
        "segment": "1",
        "name": "Prefeitura de Sapuaia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4273",
        "segment": "1",
        "name": "Prefeitura de Saquarema",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4295",
        "segment": "1",
        "name": "Prefeitura de Sen Canedo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4301",
        "segment": "1",
        "name": "Prefeitura de Sen Jose Bento",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4307",
        "segment": "1",
        "name": "Prefeitura de Senges",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4308",
        "segment": "1",
        "name": "Prefeitura de Senhor Bonfim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4311",
        "segment": "1",
        "name": "Prefeitura de Sra Dos Remedios",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4318",
        "segment": "1",
        "name": "Prefeitura de Serra Es",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4329",
        "segment": "1",
        "name": "Prefeitura de Serra Aimores",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4337",
        "segment": "1",
        "name": "Prefeitura de Serrana Sp",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4355",
        "segment": "1",
        "name": "Prefeitura de Sete Lagoas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4364",
        "segment": "1",
        "name": "Prefeitura de Silvania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4376",
        "segment": "1",
        "name": "Prefeitura de Simonesia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4391",
        "segment": "1",
        "name": "Prefeitura de Sobral",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4393",
        "segment": "1",
        "name": "Prefeitura de Socorro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4399",
        "segment": "1",
        "name": "Prefeitura de Soledade Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4404",
        "segment": "1",
        "name": "Prefeitura de Sorocaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4414",
        "segment": "1",
        "name": "Prefeitura de Sumare",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4418",
        "segment": "1",
        "name": "Prefeitura de Suzano",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4427",
        "segment": "1",
        "name": "Prefeitura de Tabuleiro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4471",
        "segment": "1",
        "name": "Prefeitura de Taquaracu Minas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4489",
        "segment": "1",
        "name": "Prefeitura de Tatui",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4497",
        "segment": "1",
        "name": "Prefeitura de Teixeira Freitas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4502",
        "segment": "1",
        "name": "Prefeitura de Telemaco Borba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4510",
        "segment": "1",
        "name": "Prefeitura de Teofilo Otoni",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4514",
        "segment": "1",
        "name": "Prefeitura de Teresina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4516",
        "segment": "1",
        "name": "Prefeitura de Teresopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4524",
        "segment": "1",
        "name": "Prefeitura de Terra Roxa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4530",
        "segment": "1",
        "name": "Prefeitura de Tibagi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4532",
        "segment": "1",
        "name": "Prefeitura de Tiete",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4539",
        "segment": "1",
        "name": "Prefeitura de Timbo Sc",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4542",
        "segment": "1",
        "name": "Prefeitura de Timon",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4543",
        "segment": "1",
        "name": "Prefeitura de Timoteo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4544",
        "segment": "1",
        "name": "Prefeitura de Tiradentes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4551",
        "segment": "1",
        "name": "Prefeitura de Toledo Pr",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4554",
        "segment": "1",
        "name": "Prefeitura de Tombos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4565",
        "segment": "1",
        "name": "Prefeitura de Trajano De Moraes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4568",
        "segment": "1",
        "name": "Prefeitura de Tremembe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4571",
        "segment": "1",
        "name": "Prefeitura de Tres Barras Paran",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4573",
        "segment": "1",
        "name": "Prefeitura de Tres Coracoes",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4577",
        "segment": "1",
        "name": "Prefeitura de Tres Lagoas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4578",
        "segment": "1",
        "name": "Prefeitura de Tres Marias",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4581",
        "segment": "1",
        "name": "Prefeitura de Tres Pontas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4586",
        "segment": "1",
        "name": "Prefeitura de Trindade",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4601",
        "segment": "1",
        "name": "Prefeitura de Tumiritinga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4630",
        "segment": "1",
        "name": "Prefeitura de Uba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4637",
        "segment": "1",
        "name": "Prefeitura de Ubatuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4641",
        "segment": "1",
        "name": "Prefeitura de Ubirata",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4652",
        "segment": "1",
        "name": "Prefeitura de Umuarama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4654",
        "segment": "1",
        "name": "Prefeitura de Unai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4667",
        "segment": "1",
        "name": "Prefeitura de Uruacu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4668",
        "segment": "1",
        "name": "Prefeitura de Uruana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4672",
        "segment": "1",
        "name": "Prefeitura de Urucania",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4683",
        "segment": "1",
        "name": "Prefeitura de Urutai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4685",
        "segment": "1",
        "name": "Prefeitura de Vacaria",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4692",
        "segment": "1",
        "name": "Prefeitura de Valinhos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4701",
        "segment": "1",
        "name": "Prefeitura de Varginha-Tributos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4704",
        "segment": "1",
        "name": "Prefeitura de Varre E Sai",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4730",
        "segment": "1",
        "name": "Prefeitura de Vera Cruz Ba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4731",
        "segment": "1",
        "name": "Prefeitura de Vera Cruz Sp",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4739",
        "segment": "1",
        "name": "Prefeitura de Vespasiano",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4748",
        "segment": "1",
        "name": "Prefeitura de Vicentinopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4750",
        "segment": "1",
        "name": "Prefeitura de Vicosa-Tributos",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4767",
        "segment": "1",
        "name": "Prefeitura de Vila Velha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4768",
        "segment": "1",
        "name": "Prefeitura de Vilhena",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4771",
        "segment": "1",
        "name": "Prefeitura de Virgem Lapa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4784",
        "segment": "1",
        "name": "Prefeitura de Vitoria",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4785",
        "segment": "1",
        "name": "Prefeitura de Vitoria Conquista",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4791",
        "segment": "1",
        "name": "Prefeitura de Volta Redonda",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4792",
        "segment": "1",
        "name": "Prefeitura de Votorantim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4797",
        "segment": "1",
        "name": "Prefeitura de Franca",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4813",
        "segment": "1",
        "name": "Prefeitura de S Fco Itabapoana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4814",
        "segment": "1",
        "name": "Prefeitura de Cocalzinho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4815",
        "segment": "1",
        "name": "Prefeitura de Macuco",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4817",
        "segment": "1",
        "name": "Prefeitura de Santana Paraiso",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4821",
        "segment": "1",
        "name": "Prefeitura de Aricanduva",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4828",
        "segment": "1",
        "name": "Prefeitura de Aperibe",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4829",
        "segment": "1",
        "name": "Prefeitura de Rio Das Ostras",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4833",
        "segment": "1",
        "name": "Prefeitura de Iguaba Grande",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4834",
        "segment": "1",
        "name": "Prefeitura de Alfredo Vasconcel",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4835",
        "segment": "1",
        "name": "Prefeitura de Alto Jequitiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4844",
        "segment": "1",
        "name": "Prefeitura de Rosario Limeira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4846",
        "segment": "1",
        "name": "Prefeitura de S Joaquim Bicas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4847",
        "segment": "1",
        "name": "Prefeitura de Tangua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4848",
        "segment": "1",
        "name": "Prefeitura de Pinheiral",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4849",
        "segment": "1",
        "name": "Prefeitura de Armacao Buzios",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4853",
        "segment": "1",
        "name": "Prefeitura de Guapimirim",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4860",
        "segment": "1",
        "name": "Prefeitura de Sarzedo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4864",
        "segment": "1",
        "name": "Prefeitura de Novo Gama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4865",
        "segment": "1",
        "name": "Prefeitura de Cid Ocidental",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4866",
        "segment": "1",
        "name": "Prefeitura de Valparaiso",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4867",
        "segment": "1",
        "name": "Prefeitura de Aguas Lindas Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4875",
        "segment": "1",
        "name": "Prefeitura de Juatuba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4876",
        "segment": "1",
        "name": "Prefeitura de S Jose Da Lapa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4878",
        "segment": "1",
        "name": "Prefeitura de Alto Caparao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4895",
        "segment": "1",
        "name": "Prefeitura de Divisopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4904",
        "segment": "1",
        "name": "Prefeitura de Guaraciama",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4926",
        "segment": "1",
        "name": "Prefeitura de Naque",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4937",
        "segment": "1",
        "name": "Prefeitura de Palmopolis",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4940",
        "segment": "1",
        "name": "Prefeitura de Periquito",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4959",
        "segment": "1",
        "name": "Prefeitura de S J Manteninha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4961",
        "segment": "1",
        "name": "Prefeitura de Sao Jose Barra",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4969",
        "segment": "1",
        "name": "Prefeitura de Ubaporanga",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5146",
        "segment": "1",
        "name": "Prefeitura de Jaiba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5181",
        "segment": "1",
        "name": "Prefeitura de Querencia",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5369",
        "segment": "1",
        "name": "Prefeitura de S Manoel Pr",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5375",
        "segment": "1",
        "name": "Prefeitura de Mesquita",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5645",
        "segment": "1",
        "name": "Prefeitura de Nova Campina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5889",
        "segment": "1",
        "name": "Prefeitura de Sao Paulo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "5896",
        "segment": "1",
        "name": "Prefeitura de Santo Andre",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "6217",
        "segment": "1",
        "name": "Prefeitura de Batatais",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "431",
        "segment": "1",
        "name": "Prefeitura de Barao",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "964",
        "segment": "1",
        "name": "Prefeitura Municial Caragua",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1057",
        "segment": "1",
        "name": "Prefeitura de Catu",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1625",
        "segment": "1",
        "name": "Prefeitura de Franco da Rocha",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1651",
        "segment": "1",
        "name": "Prefeitura de Garca Sp",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1736",
        "segment": "1",
        "name": "Prefeitura de Guanambi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "1765",
        "segment": "1",
        "name": "Prefeitura de Guarapari",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2222",
        "segment": "1",
        "name": "Prefeitura de Jandira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2296",
        "segment": "1",
        "name": "Prefeitura de Joinville",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2451",
        "segment": "1",
        "name": "Prefeitura de Louveira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2697",
        "segment": "1",
        "name": "Prefeitura de Miranda",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2882",
        "segment": "1",
        "name": "Prefeitura de N Andradina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3090",
        "segment": "1",
        "name": "Prefeitura de Panambi",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3138",
        "segment": "1",
        "name": "Prefeitura de Parauna Go",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3268",
        "segment": "1",
        "name": "Prefeitura de Pesqueira P",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3299",
        "segment": "1",
        "name": "Prefeitura de Pindamonhangaba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3380",
        "segment": "1",
        "name": "Prefeitura de Poa",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3695",
        "segment": "1",
        "name": "Prefeitura de R Vermelho",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3791",
        "segment": "1",
        "name": "Prefeitura de Sta. Barbara Oeste",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3813",
        "segment": "1",
        "name": "Prefeitura de S.C.RIO PARDO",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4424",
        "segment": "1",
        "name": "Prefeitura de Taboão da Serra",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4491",
        "segment": "1",
        "name": "Prefeitura de Taubaté",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4688",
        "segment": "1",
        "name": "Prefeitura de Valenca",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4812",
        "segment": "1",
        "name": "Prefeitura de Ilha Comprida",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "2672",
        "segment": "1",
        "name": "Prefeitura de Miguel Pereira",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3371",
        "segment": "1",
        "name": "Prefeitura de Planaltina",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3372",
        "segment": "1",
        "name": "Prefeitura de Planatina Do Parana",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3376",
        "segment": "1",
        "name": "Prefeitura de Planalto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3503",
        "segment": "1",
        "name": "Prefeitura de Presidente Olegario",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3659",
        "segment": "1",
        "name": "Prefeitura de Rio De Janeiro",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3731",
        "segment": "1",
        "name": "Prefeitura de Rubiataba",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "3958",
        "segment": "1",
        "name": "Prefeitura de S Antonio Descoberto",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4717",
        "segment": "1",
        "name": "Prefeitura de Varzea Paulista",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4769",
        "segment": "1",
        "name": "Prefeitura de Vinhedo",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4776",
        "segment": "1",
        "name": "Prefeitura de Visconde Rio Branco",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "4873",
        "segment": "1",
        "name": "Prefeitura de Entre Folhas",
        "time": "24H",
        "type": BarCodeType.iss,
    },
    {
        "code": "328",
        "segment": "5",
        "name": "Simples Nacional",
        "time": "24H",
        "type": BarCodeType.das,
    },
    {
        "code": "270",
        "segment": "5",
        "name": "INSS",
        "time": "24H",
        "type": BarCodeType.gps,
    },
    {
        "code": "9",
        "segment": "5",
        "name": "SEFAZ Distrito Federal",
        "time": "24H",
        "type": BarCodeType.darf,
    },
    {
        "code": "64",
        "segment": "5",
        "name": "Receita Federal",
        "time": "24H",
        "type": BarCodeType.darf,
    },
    {
        "code": "123",
        "segment": "5",
        "name": "SEFAZ Mato Grosso",
        "time": "24H",
        "type": BarCodeType.darf,
    },
    {
        "code": "385",
        "segment": "5",
        "name": "Receita Federal",
        "time": "24H",
        "type": BarCodeType.darf,
    },
    {
        "code": "24",
        "segment": "5",
        "name": "SEFAZ Santa Catarina",
        "time": "24H",
        "type": BarCodeType.darf,
    },
    {
        "code": "185",
        "segment": "5",
        "name": "SEFAZ São Paulo",
        "time": "24H",
        "type": BarCodeType.dare,
    },
    {
        "code": "6",
        "segment": "5",
        "name": "SEFAZ Ceará",
        "time": "24H",
        "type": BarCodeType.dae,
    },
    {
        "code": "179",
        "segment": "5",
        "name": "FGTS",
        "time": "24H",
        "type": BarCodeType.fgts,
    },
    {
        "code": "239",
        "segment": "5",
        "name": "FGTS",
        "time": "24H",
        "type": BarCodeType.fgts,
    },
    {
        "code": "90",
        "segment": "5",
        "name": "SEFAZ Paraná",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "94",
        "segment": "5",
        "name": "SEFAZ Rio Grande do Norte",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "98",
        "segment": "5",
        "name": "SEFAZ Santa Catarina",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "291",
        "segment": "5",
        "name": "SEFAZ Alagoas",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "292",
        "segment": "5",
        "name": "SEFAZ Amapá",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "294",
        "segment": "5",
        "name": "SEFAZ Bahia",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "295",
        "segment": "5",
        "name": "SEFAZ Ceará",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "297",
        "segment": "5",
        "name": "SEFAZ Goiás",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "300",
        "segment": "5",
        "name": "SEFAZ Mato Grosso",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "301",
        "segment": "5",
        "name": "SEFAZ Mato Grosso do Sul",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "302",
        "segment": "5",
        "name": "SEFAZ Minas Gerais",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "303",
        "segment": "5",
        "name": "SEFAZ Pará",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "304",
        "segment": "5",
        "name": "SEFAZ Paraíba",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "306",
        "segment": "5",
        "name": "SEFAZ Pernambuco",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "307",
        "segment": "5",
        "name": "SEFAZ Piauí",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "310",
        "segment": "5",
        "name": "SEFAZ Rio Grande do Sul",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "99",
        "segment": "5",
        "name": "SEFAZ São Paulo",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "96",
        "segment": "5",
        "name": "SEFAZ Rondônia",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "293",
        "segment": "5",
        "name": "SEFAZ Amazonas",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "298",
        "segment": "5",
        "name": "SEFAZ Distrito Federal",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "299",
        "segment": "5",
        "name": "SEFAZ Maranhão",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "278",
        "segment": "5",
        "name": "SEFAZ Rio de Janeiro",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "315",
        "segment": "5",
        "name": "SEFAZ Sergipe",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "316",
        "segment": "5",
        "name": "SEFAZ Tocantins",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "260",
        "segment": "5",
        "name": "SEFAZ Paraíba",
        "time": "24H",
        "type": BarCodeType.gnre,
    },
    {
        "code": "79",
        "segment": "5",
        "name": "DAE RECEBIVEIS",
        "type": BarCodeType.dae,
    },
    {
        "code": "240",
        "segment": "5",
        "name": "FGTS-GRDE",
        "type": BarCodeType.fgts,
    },
    {
        "code": "221",
        "segment": "5",
        "name": "SEFAZ-MG/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "27",
        "segment": "5",
        "name": "SEFAZ-TO/DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "174",
        "segment": "5",
        "name": "SEFAZ-TO/DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "173",
        "segment": "5",
        "name": "SEFAZ-TO-DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "451",
        "segment": "5",
        "name": "FGTS",
        "type": BarCodeType.fgts,
    },
    {
        "code": "192",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "191",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "175",
        "segment": "5",
        "name": "SEFAZ-TO/DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "181",
        "segment": "5",
        "name": "FGTS-GRF",
        "type": BarCodeType.fgts,
    },
    {
        "code": "153",
        "segment": "5",
        "name": "DARF",
        "type": BarCodeType.darf,
    },
    {
        "code": "193",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "8",
        "segment": "5",
        "name": "SEFAZ-GO/DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "180",
        "segment": "5",
        "name": "FGTS-GRF",
        "type": BarCodeType.fgts,
    },
    {
        "code": "10",
        "segment": "5",
        "name": "SEFAZ-MA/DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "134",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "5",
        "segment": "5",
        "name": "SEFAZ-BA/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "124",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "257",
        "segment": "5",
        "name": "SEFAZ SE DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "213",
        "segment": "5",
        "name": "SEFAZ-MG/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "768",
        "segment": "5",
        "name": "SEFAZ RR DARE",
        "type": BarCodeType.dare,
    },
    {
        "code": "60",
        "segment": "5",
        "name": "SEFAZ-MG/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "103",
        "segment": "5",
        "name": "SEFAZ-PE/DAE",
        "type": BarCodeType.dae,
    },
    {
        "code": "312",
        "segment": "5",
        "name": "GNRE-RR",
        "type": BarCodeType.gnre,
    },
    {
        "code": "333",
        "segment": "5",
        "name": "SEFAZ-BA DAE N TRIBU",
        "type": BarCodeType.dae,
    },
    {
        "code": "130",
        "segment": "5",
        "name": "SEFAZ BA DAE IPVA",
        "type": BarCodeType.dae,
    },
    {
        "code": "115",
        "segment": "5",
        "name": "SEFAZ-MG/DAE",
        "type": BarCodeType.dae,
    },
]
utilities = [
    {
        "code": "0",
        "segment": "7",
        "name": "SAO PAULO-MULTA",
        "time": "24H"
    },
    {
        "code": "1",
        "segment": "3",
        "name": "ENERGISA SUL SUDESTE",
        "time": "24H"
    },
    {
        "code": "2",
        "segment": "2",
        "name": "CAEMA MARANHAO",
        "time": "24H"
    },
    {
        "code": "2",
        "segment": "3",
        "name": "CEA ELETRIC AMAPA",
        "time": "24H"
    },
    {
        "code": "2",
        "segment": "4",
        "name": "BRASIL TELECOM-RS",
        "time": "24H"
    },
    {
        "code": "2",
        "segment": "5",
        "name": "SEFAZ-AL/DAR",
        "time": "24H"
    },
    {
        "code": "3",
        "segment": "3",
        "name": "EQUATORIAL ALAGOAS",
        "time": "24H"
    },
    {
        "code": "3",
        "segment": "5",
        "name": "SEFAZ-AP",
        "time": "24H"
    },
    {
        "code": "4",
        "segment": "2",
        "name": "CAER",
        "time": "24H"
    },
    {
        "code": "4",
        "segment": "4",
        "name": "ALGAR TELECOM",
        "time": "24H"
    },
    {
        "code": "4",
        "segment": "5",
        "name": "SEFAZ-AM",
        "time": "24H"
    },
    {
        "code": "5",
        "segment": "2",
        "name": "CAERD",
        "time": "24H"
    },
    {
        "code": "5",
        "segment": "3",
        "name": "NEOENERGIA BRASILIA",
        "time": "24H"
    },
    {
        "code": "5",
        "segment": "4",
        "name": "BRASIL TELECOM-PELOT",
        "time": "24H"
    },
    {
        "code": "6",
        "segment": "2",
        "name": "CAERN",
        "time": "24H"
    },
    {
        "code": "6",
        "segment": "3",
        "name": "CEEE DISTRIBUICAO",
        "time": "24H"
    },
    {
        "code": "6",
        "segment": "4",
        "name": "EMBRATEL",
        "time": "24H"
    },
    {
        "code": "7",
        "segment": "2",
        "name": "CAESA",
        "time": "24H"
    },
    {
        "code": "7",
        "segment": "3",
        "name": "ENERGISA-BORBOREMA",
        "time": "24H"
    },
    {
        "code": "7",
        "segment": "4",
        "name": "SERCOMTEL",
        "time": "24H"
    },
    {
        "code": "7",
        "segment": "5",
        "name": "SEFAZ-ES/DUA",
        "time": "24H"
    },
    {
        "code": "8",
        "segment": "2",
        "name": "CAESB",
        "time": "24H"
    },
    {
        "code": "9",
        "segment": "2",
        "name": "CAGECE",
        "time": "24H"
    },
    {
        "code": "9",
        "segment": "3",
        "name": "EQUATORIAL GOIAS",
        "time": "24H"
    },
    {
        "code": "10",
        "segment": "2",
        "name": "CAGEPA",
        "time": "24H"
    },
    {
        "code": "10",
        "segment": "3",
        "name": "EQUATORIAL PARA",
        "time": "24H"
    },
    {
        "code": "816",
        "segment": "2",
        "name": "SAMAE TIMBO",
        "time": "15H"
    },
    {
        "code": "11",
        "segment": "3",
        "name": "CELPE",
        "time": "24H"
    },
    {
        "code": "11",
        "segment": "4",
        "name": "BRASIL TELECOM-AC",
        "time": "24H"
    },
    {
        "code": "12",
        "segment": "3",
        "name": "ENERGISA TO",
        "time": "24H"
    },
    {
        "code": "12",
        "segment": "5",
        "name": "SEFAZ-MS",
        "time": "24H"
    },
    {
        "code": "13",
        "segment": "2",
        "name": "CASAN",
        "time": "24H"
    },
    {
        "code": "13",
        "segment": "3",
        "name": "EQUATORIAL MARANHAO",
        "time": "24H"
    },
    {
        "code": "14",
        "segment": "2",
        "name": "CEDAE",
        "time": "24H"
    },
    {
        "code": "14",
        "segment": "3",
        "name": "ENERGISA MT",
        "time": "24H"
    },
    {
        "code": "14",
        "segment": "4",
        "name": "BRASIL TELECOM-DF",
        "time": "24H"
    },
    {
        "code": "15",
        "segment": "2",
        "name": "CESAMA",
        "time": "24H"
    },
    {
        "code": "15",
        "segment": "5",
        "name": "SEFAZ PB ITCD",
        "time": "24H"
    },
    {
        "code": "16",
        "segment": "2",
        "name": "CESAN",
        "time": "24H"
    },
    {
        "code": "16",
        "segment": "3",
        "name": "ENERGISA N FRIBURGO",
        "time": "24H"
    },
    {
        "code": "16",
        "segment": "4",
        "name": "BRASIL TELECOM-GO",
        "time": "24H"
    },
    {
        "code": "16",
        "segment": "5",
        "name": "DETRAN-PR-GRM",
        "time": "24H"
    },
    {
        "code": "17",
        "segment": "3",
        "name": "EQUATORIAL PIAUI",
        "time": "20H"
    },
    {
        "code": "17",
        "segment": "4",
        "name": "BRASIL TELECOM-MT",
        "time": "20H"
    },
    {
        "code": "18",
        "segment": "2",
        "name": "COMPESA",
        "time": "24H"
    },
    {
        "code": "18",
        "segment": "3",
        "name": "CERIPA",
        "time": "24H"
    },
    {
        "code": "18",
        "segment": "5",
        "name": "SEFAZ-PI/ITCMD",
        "time": "24H"
    },
    {
        "code": "19",
        "segment": "2",
        "name": "COPASA",
        "time": "24H"
    },
    {
        "code": "19",
        "segment": "3",
        "name": "AMPLA",
        "time": "24H"
    },
    {
        "code": "19",
        "segment": "4",
        "name": "BRASIL TELECOM-MS",
        "time": "24H"
    },
    {
        "code": "20",
        "segment": "3",
        "name": "ENERGISA RO",
        "time": "24H"
    },
    {
        "code": "20",
        "segment": "4",
        "name": "BRASIL TELECOM-PR",
        "time": "24H"
    },
    {
        "code": "22",
        "segment": "2",
        "name": "COSANPA",
        "time": "24H"
    },
    {
        "code": "22",
        "segment": "3",
        "name": "ELEKTRO",
        "time": "24H"
    },
    {
        "code": "23",
        "segment": "2",
        "name": "SAE ARAGUARI",
        "time": "24H"
    },
    {
        "code": "23",
        "segment": "3",
        "name": "CHESP",
        "time": "24H"
    },
    {
        "code": "23",
        "segment": "5",
        "name": "IPVA RR",
        "time": "24H"
    },
    {
        "code": "23",
        "segment": "6",
        "name": "PAGNOMINAL-MAIS DOMI",
        "time": "24H"
    },
    {
        "code": "24",
        "segment": "2",
        "name": "DAAE ARARAQUARA",
        "time": "24H"
    },
    {
        "code": "24",
        "segment": "3",
        "name": "ENERGISA-MG",
        "time": "24H"
    },
    {
        "code": "24",
        "segment": "4",
        "name": "OI S.A.",
        "time": "24H"
    },
    {
        "code": "25",
        "segment": "3",
        "name": "REDE CFLO",
        "time": "24H"
    },
    {
        "code": "25",
        "segment": "5",
        "name": "GARE IPVA",
        "time": "24H"
    },
    {
        "code": "26",
        "segment": "2",
        "name": "DAAE RIO CLARO",
        "time": "24H"
    },
    {
        "code": "26",
        "segment": "3",
        "name": "CPFL LUZ MOCOCA",
        "time": "24H"
    },
    {
        "code": "26",
        "segment": "4",
        "name": "BRASIL TELECOM-RO",
        "time": "24H"
    },
    {
        "code": "27",
        "segment": "2",
        "name": "DAE AMERICANA",
        "time": "24H"
    },
    {
        "code": "27",
        "segment": "3",
        "name": "CLFSC",
        "time": "24H"
    },
    {
        "code": "27",
        "segment": "4",
        "name": "BRASIL TELECOM-SC",
        "time": "24H"
    },
    {
        "code": "28",
        "segment": "3",
        "name": "REDE CNEE",
        "time": "24H"
    },
    {
        "code": "29",
        "segment": "2",
        "name": "DAE BAURU",
        "time": "24H"
    },
    {
        "code": "29",
        "segment": "3",
        "name": "COCEL",
        "time": "24H"
    },
    {
        "code": "29",
        "segment": "4",
        "name": "TELEFONICA SP",
        "time": "24H"
    },
    {
        "code": "30",
        "segment": "3",
        "name": "COELBA",
        "time": "24H"
    },
    {
        "code": "31",
        "segment": "2",
        "name": "DAE JUNDIAI",
        "time": "24H"
    },
    {
        "code": "31",
        "segment": "3",
        "name": "COELCE",
        "time": "24H"
    },
    {
        "code": "32",
        "segment": "2",
        "name": "DAEM-MARILIA",
        "time": "24H"
    },
    {
        "code": "33",
        "segment": "2",
        "name": "DAE STA BARBARA",
        "time": "24H"
    },
    {
        "code": "34",
        "segment": "2",
        "name": "DAE SANTANA LIVRAMEN",
        "time": "24H"
    },
    {
        "code": "35",
        "segment": "2",
        "name": "SAESA",
        "time": "24H"
    },
    {
        "code": "35",
        "segment": "6",
        "name": "INFRAERO",
        "time": "24H"
    },
    {
        "code": "37",
        "segment": "2",
        "name": "DAEV",
        "time": "24H"
    },
    {
        "code": "38",
        "segment": "3",
        "name": "COSERN",
        "time": "24H"
    },
    {
        "code": "39",
        "segment": "2",
        "name": "DAEMO OLIMPIA",
        "time": "24H"
    },
    {
        "code": "39",
        "segment": "3",
        "name": "CPFL LESTE PTA",
        "time": "24H"
    },
    {
        "code": "40",
        "segment": "2",
        "name": "SAERP RIB P",
        "time": "24H"
    },
    {
        "code": "40",
        "segment": "3",
        "name": "CPFL PAULISTA",
        "time": "24H"
    },
    {
        "code": "41",
        "segment": "2",
        "name": "DESO",
        "time": "24H"
    },
    {
        "code": "41",
        "segment": "3",
        "name": "DME POCOS DE CALDAS",
        "time": "24H"
    },
    {
        "code": "41",
        "segment": "4",
        "name": "VIVO-BA",
        "time": "24H"
    },
    {
        "code": "42",
        "segment": "2",
        "name": "DMAE POCOS DE CALDAS",
        "time": "24H"
    },
    {
        "code": "42",
        "segment": "3",
        "name": "REDE EMPR BRAGANTINA",
        "time": "24H"
    },
    {
        "code": "42",
        "segment": "4",
        "name": "VIVO-SE",
        "time": "24H"
    },
    {
        "code": "43",
        "segment": "2",
        "name": "DMAE PORTO ALEGRE",
        "time": "24H"
    },
    {
        "code": "43",
        "segment": "3",
        "name": "REDE EEVP",
        "time": "24H"
    },
    {
        "code": "44",
        "segment": "2",
        "name": "DMAE UBERLANDIA",
        "time": "24H"
    },
    {
        "code": "44",
        "segment": "3",
        "name": "ELF SANTA MARIA",
        "time": "24H"
    },
    {
        "code": "44",
        "segment": "4",
        "name": "VIVO-GO",
        "time": "24H"
    },
    {
        "code": "46",
        "segment": "3",
        "name": "ELETROCAR",
        "time": "24H"
    },
    {
        "code": "47",
        "segment": "2",
        "name": "EMBASA",
        "time": "24H"
    },
    {
        "code": "47",
        "segment": "3",
        "name": "AMAZONAS ENERGIA",
        "time": "24H"
    },
    {
        "code": "47",
        "segment": "4",
        "name": "VIVO-DF",
        "time": "24H"
    },
    {
        "code": "48",
        "segment": "3",
        "name": "ELETROPAULO",
        "time": "24H"
    },
    {
        "code": "48",
        "segment": "4",
        "name": "VIVO-RJ",
        "time": "24H"
    },
    {
        "code": "49",
        "segment": "3",
        "name": "ENERGISA-SE",
        "time": "20H"
    },
    {
        "code": "49",
        "segment": "4",
        "name": "VIVO-MS",
        "time": "20H"
    },
    {
        "code": "50",
        "segment": "2",
        "name": "SAAE AGUAS LINDOIA",
        "time": "24H"
    },
    {
        "code": "50",
        "segment": "3",
        "name": "ENERGISA MS",
        "time": "24H"
    },
    {
        "code": "51",
        "segment": "2",
        "name": "SAAE AMPARO",
        "time": "24H"
    },
    {
        "code": "51",
        "segment": "3",
        "name": "EDP ES",
        "time": "24H"
    },
    {
        "code": "52",
        "segment": "2",
        "name": "SAAE ARACRUZ",
        "time": "24H"
    },
    {
        "code": "52",
        "segment": "3",
        "name": "CPFL CIA JAGUARI",
        "time": "24H"
    },
    {
        "code": "52",
        "segment": "5",
        "name": "GARE PPD",
        "time": "24H"
    },
    {
        "code": "53",
        "segment": "2",
        "name": "SAAE ATIBAIA",
        "time": "24H"
    },
    {
        "code": "53",
        "segment": "3",
        "name": "LIGHT",
        "time": "24H"
    },
    {
        "code": "53",
        "segment": "4",
        "name": "VIVO-AC",
        "time": "24H"
    },
    {
        "code": "53",
        "segment": "5",
        "name": "SEFAZ SAO PAULO-MILT-CB",
        "time": "24H"
    },
    {
        "code": "54",
        "segment": "3",
        "name": "ENERGISA-PB",
        "time": "20H"
    },
    {
        "code": "55",
        "segment": "2",
        "name": "S BARRA BONITA",
        "time": "24H"
    },
    {
        "code": "55",
        "segment": "3",
        "name": "CPFL SUL PTA",
        "time": "24H"
    },
    {
        "code": "55",
        "segment": "4",
        "name": "VIVO-MT",
        "time": "24H"
    },
    {
        "code": "56",
        "segment": "2",
        "name": "SAAE BARRETOS",
        "time": "24H"
    },
    {
        "code": "56",
        "segment": "3",
        "name": "CEG",
        "time": "24H"
    },
    {
        "code": "57",
        "segment": "3",
        "name": "COMGAS",
        "time": "24H"
    },
    {
        "code": "58",
        "segment": "4",
        "name": "VIVO-RO",
        "time": "24H"
    },
    {
        "code": "59",
        "segment": "2",
        "name": "BRK CACHOEIRO",
        "time": "24H"
    },
    {
        "code": "60",
        "segment": "2",
        "name": "SAAE CACOAL",
        "time": "24H"
    },
    {
        "code": "60",
        "segment": "4",
        "name": "VIVO-ES",
        "time": "24H"
    },
    {
        "code": "61",
        "segment": "3",
        "name": "CEMIRIM",
        "time": "24H"
    },
    {
        "code": "61",
        "segment": "5",
        "name": "IPVA-MG ATU",
        "time": "24H"
    },
    {
        "code": "61",
        "segment": "6",
        "name": "PROCON RIO VERDE",
        "time": "24H"
    },
    {
        "code": "62",
        "segment": "2",
        "name": "SAAE CAPIVARI",
        "time": "24H"
    },
    {
        "code": "63",
        "segment": "5",
        "name": "IPVA-MG ANT",
        "time": "24H"
    },
    {
        "code": "64",
        "segment": "4",
        "name": "VIVO-MG",
        "time": "24H"
    },
    {
        "code": "67",
        "segment": "2",
        "name": "SAAE FORMIGA",
        "time": "24H"
    },
    {
        "code": "67",
        "segment": "3",
        "name": "DEMEI IJUI",
        "time": "24H"
    },
    {
        "code": "68",
        "segment": "2",
        "name": "SAAE GARCA",
        "time": "24H"
    },
    {
        "code": "69",
        "segment": "4",
        "name": "VIVO-PR/SC",
        "time": "24H"
    },
    {
        "code": "70",
        "segment": "2",
        "name": "SAEG GUARATINGUETA",
        "time": "24H"
    },
    {
        "code": "71",
        "segment": "2",
        "name": "S.INDAIATUBA",
        "time": "24H"
    },
    {
        "code": "71",
        "segment": "4",
        "name": "CLARO FIXO SA",
        "time": "24H"
    },
    {
        "code": "72",
        "segment": "2",
        "name": "SAAE ITAPIRA",
        "time": "24H"
    },
    {
        "code": "72",
        "segment": "4",
        "name": "VIVO-PA",
        "time": "24H"
    },
    {
        "code": "73",
        "segment": "3",
        "name": "EDP SAO PAULO",
        "time": "24H"
    },
    {
        "code": "73",
        "segment": "4",
        "name": "VIVO-AM",
        "time": "24H"
    },
    {
        "code": "74",
        "segment": "2",
        "name": "SAE ITUIUTABA",
        "time": "24H"
    },
    {
        "code": "74",
        "segment": "3",
        "name": "COOP ALIANCA",
        "time": "24H"
    },
    {
        "code": "74",
        "segment": "4",
        "name": "VIVO-MA",
        "time": "24H"
    },
    {
        "code": "75",
        "segment": "2",
        "name": "SAAE JABOTICABAL",
        "time": "24H"
    },
    {
        "code": "75",
        "segment": "3",
        "name": "RORAIMA ENERGIA",
        "time": "24H"
    },
    {
        "code": "75",
        "segment": "4",
        "name": "VIVO-RR",
        "time": "24H"
    },
    {
        "code": "76",
        "segment": "2",
        "name": "SAAE JACAREI",
        "time": "24H"
    },
    {
        "code": "76",
        "segment": "4",
        "name": "VIVO-AP",
        "time": "24H"
    },
    {
        "code": "77",
        "segment": "2",
        "name": "SAAE L.PAULISTA",
        "time": "24H"
    },
    {
        "code": "77",
        "segment": "3",
        "name": "COMPAGAS",
        "time": "24H"
    },
    {
        "code": "77",
        "segment": "4",
        "name": "TIM S/A",
        "time": "24H"
    },
    {
        "code": "78",
        "segment": "4",
        "name": "CLARO FIXO SP",
        "time": "24H"
    },
    {
        "code": "79",
        "segment": "2",
        "name": "SAAE LINHARES",
        "time": "24H"
    },
    {
        "code": "79",
        "segment": "4",
        "name": "VIVO-RS",
        "time": "24H"
    },
    {
        "code": "80",
        "segment": "3",
        "name": "CERMESO",
        "time": "24H"
    },
    {
        "code": "80",
        "segment": "4",
        "name": "VIVO-SP",
        "time": "24H"
    },
    {
        "code": "81",
        "segment": "2",
        "name": "SAAE MOGI MIRIM",
        "time": "24H"
    },
    {
        "code": "81",
        "segment": "4",
        "name": "VIVO-TO",
        "time": "24H"
    },
    {
        "code": "82",
        "segment": "3",
        "name": "CEREJ",
        "time": "24H"
    },
    {
        "code": "82",
        "segment": "4",
        "name": "VIVO FIXO NAC 13 DIG",
        "time": "24H"
    },
    {
        "code": "84",
        "segment": "4",
        "name": "TELEFONICA EMPRESAS",
        "time": "24H"
    },
    {
        "code": "85",
        "segment": "2",
        "name": "SAAE PASSOS",
        "time": "24H"
    },
    {
        "code": "86",
        "segment": "2",
        "name": "SANEP",
        "time": "24H"
    },
    {
        "code": "86",
        "segment": "3",
        "name": "RGE SUL",
        "time": "24H"
    },
    {
        "code": "87",
        "segment": "2",
        "name": "SAAE PROMISSAO",
        "time": "24H"
    },
    {
        "code": "89",
        "segment": "2",
        "name": "SAAE SAO CARLOS",
        "time": "24H"
    },
    {
        "code": "89",
        "segment": "3",
        "name": "RGE",
        "time": "24H"
    },
    {
        "code": "89",
        "segment": "4",
        "name": "NEXTEL",
        "time": "24H"
    },
    {
        "code": "89",
        "segment": "5",
        "name": "SEFAZ PB FEEF",
        "time": "24H"
    },
    {
        "code": "91",
        "segment": "2",
        "name": "SAAE SOROCABA",
        "time": "24H"
    },
    {
        "code": "92",
        "segment": "2",
        "name": "SAAET-TAQUARITINGA",
        "time": "24H"
    },
    {
        "code": "93",
        "segment": "2",
        "name": "SAAE UNAI",
        "time": "24H"
    },
    {
        "code": "93",
        "segment": "3",
        "name": "ENERGISA TO",
        "time": "24H"
    },
    {
        "code": "94",
        "segment": "2",
        "name": "SAAE VICOSA",
        "time": "24H"
    },
    {
        "code": "95",
        "segment": "2",
        "name": "SAAE VOLTA REDONDA",
        "time": "24H"
    },
    {
        "code": "96",
        "segment": "2",
        "name": "SAAETRI",
        "time": "24H"
    },
    {
        "code": "97",
        "segment": "2",
        "name": "SABESP",
        "time": "24H"
    },
    {
        "code": "97",
        "segment": "3",
        "name": "COOPERNORTE",
        "time": "24H"
    },
    {
        "code": "98",
        "segment": "2",
        "name": "SAECIL",
        "time": "24H"
    },
    {
        "code": "99",
        "segment": "2",
        "name": "SAEMA ARARAS",
        "time": "24H"
    },
    {
        "code": "100",
        "segment": "3",
        "name": "CEG RIO(REG RESENDE)",
        "time": "24H"
    },
    {
        "code": "101",
        "segment": "2",
        "name": "SAMAE JARAGUA DO SUL",
        "time": "24H"
    },
    {
        "code": "102",
        "segment": "2",
        "name": "SAMAE MOGI GUACU",
        "time": "24H"
    },
    {
        "code": "103",
        "segment": "2",
        "name": "SAMAE TIETE",
        "time": "24H"
    },
    {
        "code": "104",
        "segment": "5",
        "name": "DETRAN-PE",
        "time": "24H"
    },
    {
        "code": "105",
        "segment": "2",
        "name": "SANASA",
        "time": "24H"
    },
    {
        "code": "106",
        "segment": "2",
        "name": "SANEAGO",
        "time": "24H"
    },
    {
        "code": "106",
        "segment": "4",
        "name": "LIGGA TELECOM",
        "time": "24H"
    },
    {
        "code": "107",
        "segment": "2",
        "name": "SANEATINS",
        "time": "24H"
    },
    {
        "code": "109",
        "segment": "2",
        "name": "SANEPAR",
        "time": "20H"
    },
    {
        "code": "109",
        "segment": "3",
        "name": "CERIS",
        "time": "20H"
    },
    {
        "code": "109",
        "segment": "4",
        "name": "TIM CELULAR SA",
        "time": "20H"
    },
    {
        "code": "110",
        "segment": "2",
        "name": "SANESUL",
        "time": "24H"
    },
    {
        "code": "110",
        "segment": "3",
        "name": "CPFL PIRATININGA",
        "time": "24H"
    },
    {
        "code": "111",
        "segment": "2",
        "name": "SEMAE MOGI CRUZES",
        "time": "24H"
    },
    {
        "code": "111",
        "segment": "3",
        "name": "COPEL DISTRIBUICAO",
        "time": "24H"
    },
    {
        "code": "112",
        "segment": "2",
        "name": "SEMAE SAO LEOPOLDO",
        "time": "24H"
    },
    {
        "code": "112",
        "segment": "6",
        "name": "DAWLOG",
        "time": "24H"
    },
    {
        "code": "113",
        "segment": "2",
        "name": "SEMASA",
        "time": "24H"
    },
    {
        "code": "113",
        "segment": "4",
        "name": "OI S.A. MOVEL",
        "time": "24H"
    },
    {
        "code": "114",
        "segment": "2",
        "name": "SIMAE JOACABA",
        "time": "24H"
    },
    {
        "code": "114",
        "segment": "4",
        "name": "IDT BRASIL TELEC",
        "time": "24H"
    },
    {
        "code": "115",
        "segment": "2",
        "name": "SAE OURINHOS",
        "time": "24H"
    },
    {
        "code": "116",
        "segment": "2",
        "name": "SAEV",
        "time": "24H"
    },
    {
        "code": "116",
        "segment": "3",
        "name": "GAS NATURAL SP",
        "time": "24H"
    },
    {
        "code": "116",
        "segment": "6",
        "name": "FMMA LUZIANIA GO",
        "time": "24H"
    },
    {
        "code": "117",
        "segment": "5",
        "name": "SEFAZ-MT/DAR",
        "time": "24H"
    },
    {
        "code": "119",
        "segment": "2",
        "name": "SAMAE BRUSQUE",
        "time": "24H"
    },
    {
        "code": "119",
        "segment": "3",
        "name": "CERVAM",
        "time": "24H"
    },
    {
        "code": "119",
        "segment": "5",
        "name": "SEFAZ RR TAXAS",
        "time": "24H"
    },
    {
        "code": "120",
        "segment": "2",
        "name": "SAMAE SAO BENTO SUL",
        "time": "24H"
    },
    {
        "code": "120",
        "segment": "4",
        "name": "TRANSIT DO BRASIL",
        "time": "24H"
    },
    {
        "code": "121",
        "segment": "2",
        "name": "SEMAE PIRACICABA",
        "time": "24H"
    },
    {
        "code": "123",
        "segment": "3",
        "name": "GAS BRASILIANO",
        "time": "24H"
    },
    {
        "code": "124",
        "segment": "2",
        "name": "BRK LIMEIRA",
        "time": "24H"
    },
    {
        "code": "125",
        "segment": "3",
        "name": "CERRP",
        "time": "24H"
    },
    {
        "code": "125",
        "segment": "4",
        "name": "CLARO FIXO SP CORP",
        "time": "24H"
    },
    {
        "code": "126",
        "segment": "2",
        "name": "SAEP-PIRASSUNUNGA",
        "time": "24H"
    },
    {
        "code": "126",
        "segment": "4",
        "name": "ARO FIXO SA CORP",
        "time": "24H"
    },
    {
        "code": "127",
        "segment": "3",
        "name": "BAHIAGAS",
        "time": "24H"
    },
    {
        "code": "129",
        "segment": "2",
        "name": "SAAE ALAGOINHAS",
        "time": "24H"
    },
    {
        "code": "131",
        "segment": "3",
        "name": "CERR RORAIMA",
        "time": "24H"
    },
    {
        "code": "134",
        "segment": "2",
        "name": "SAAE ITAPETINGA",
        "time": "24H"
    },
    {
        "code": "135",
        "segment": "2",
        "name": "SAAE JUAZEIRO",
        "time": "20H"
    },
    {
        "code": "135",
        "segment": "3",
        "name": "COOPERSUL",
        "time": "20H"
    },
    {
        "code": "136",
        "segment": "3",
        "name": "COOP CASTROLANDA",
        "time": "24H"
    },
    {
        "code": "137",
        "segment": "3",
        "name": "ULTRAGAZ",
        "time": "24H"
    },
    {
        "code": "138",
        "segment": "3",
        "name": "CEMIG DISTRIBUICAO",
        "time": "24H"
    },
    {
        "code": "138",
        "segment": "5",
        "name": "SEFAZ-PA/ICMS",
        "time": "24H"
    },
    {
        "code": "139",
        "segment": "2",
        "name": "SAAE VALENCA",
        "time": "24H"
    },
    {
        "code": "139",
        "segment": "5",
        "name": "SEFAZ-PA/IPVA",
        "time": "24H"
    },
    {
        "code": "140",
        "segment": "5",
        "name": "SEFAZ-PA/D.REC.",
        "time": "24H"
    },
    {
        "code": "141",
        "segment": "5",
        "name": "SEFAZ-BA/ITCD",
        "time": "24H"
    },
    {
        "code": "142",
        "segment": "5",
        "name": "SEFAZ-BA/OUTRAS REC",
        "time": "24H"
    },
    {
        "code": "145",
        "segment": "3",
        "name": "ENERGISA-MG-FIDC",
        "time": "24H"
    },
    {
        "code": "146",
        "segment": "3",
        "name": "ENERGISA-NF-FIDC",
        "time": "20H"
    },
    {
        "code": "147",
        "segment": "3",
        "name": "ENERGISA-BOR-FIDC",
        "time": "20H"
    },
    {
        "code": "148",
        "segment": "3",
        "name": "ENERGISA-SE-FIDC",
        "time": "24H"
    },
    {
        "code": "149",
        "segment": "3",
        "name": "ENERGISA-PB-FIDC",
        "time": "20H"
    },
    {
        "code": "153",
        "segment": "2",
        "name": "SAMAE RIO NEGRINHO",
        "time": "24H"
    },
    {
        "code": "154",
        "segment": "3",
        "name": "ENERGISA MT",
        "time": "24H"
    },
    {
        "code": "155",
        "segment": "3",
        "name": "ENERGISA SUL SUDESTE",
        "time": "24H"
    },
    {
        "code": "155",
        "segment": "4",
        "name": "BRASIL TELEC CEL-RS",
        "time": "24H"
    },
    {
        "code": "156",
        "segment": "2",
        "name": "SAAE BARRA MANSA",
        "time": "24H"
    },
    {
        "code": "157",
        "segment": "2",
        "name": "SANEBAVI-VINHEDO",
        "time": "24H"
    },
    {
        "code": "158",
        "segment": "2",
        "name": "SAMAE GASPAR",
        "time": "24H"
    },
    {
        "code": "158",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "159",
        "segment": "3",
        "name": "ENERGISA MT",
        "time": "24H"
    },
    {
        "code": "159",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "160",
        "segment": "2",
        "name": "SAAE PORTO FELIZ",
        "time": "24H"
    },
    {
        "code": "160",
        "segment": "3",
        "name": "EQUATORIAL PARA",
        "time": "24H"
    },
    {
        "code": "160",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "160",
        "segment": "5",
        "name": "SEFAZ-BA/ICMS ADIC",
        "time": "24H"
    },
    {
        "code": "161",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "161",
        "segment": "5",
        "name": "TAXA RENOVACAO LICENCIAMENTO-MG - CB",
        "time": "24H"
    },
    {
        "code": "162",
        "segment": "3",
        "name": "CELESC DISTRIBUICAO",
        "time": "24H"
    },
    {
        "code": "162",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "163",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "165",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "165",
        "segment": "5",
        "name": "CBMMG",
        "time": "24H"
    },
    {
        "code": "166",
        "segment": "4",
        "name": "OI S.A. MOVEL",
        "time": "24H"
    },
    {
        "code": "173",
        "segment": "3",
        "name": "ENERGISA TO",
        "time": "24H"
    },
    {
        "code": "178",
        "segment": "2",
        "name": "SAAE LUCAS RIO VERDE",
        "time": "24H"
    },
    {
        "code": "178",
        "segment": "3",
        "name": "LIQUIGAS",
        "time": "24H"
    },
    {
        "code": "182",
        "segment": "3",
        "name": "BRASILGAS",
        "time": "24H"
    },
    {
        "code": "185",
        "segment": "3",
        "name": "CETRIL IBIUNA",
        "time": "24H"
    },
    {
        "code": "186",
        "segment": "5",
        "name": "SEFAZ PB ICMS",
        "time": "24H"
    },
    {
        "code": "187",
        "segment": "3",
        "name": "CLAYTON GAS",
        "time": "24H"
    },
    {
        "code": "192",
        "segment": "3",
        "name": "SUPERGASBRAS",
        "time": "24H"
    },
    {
        "code": "194",
        "segment": "4",
        "name": "BRASIL TEL COM",
        "time": "24H"
    },
    {
        "code": "197",
        "segment": "3",
        "name": "MINASGASBRAS",
        "time": "24H"
    },
    {
        "code": "199",
        "segment": "2",
        "name": "SAAE CATU",
        "time": "24H"
    },
    {
        "code": "199",
        "segment": "3",
        "name": "ENERGISA MS",
        "time": "24H"
    },
    {
        "code": "201",
        "segment": "5",
        "name": "SEFAZ PB OUTROS TRIB",
        "time": "24H"
    },
    {
        "code": "203",
        "segment": "7",
        "name": "Prefeitura de Andradas Multas",
        "time": "24H"
    },
    {
        "code": "209",
        "segment": "6",
        "name": "ASSOC N S FATIMA",
        "time": "24H"
    },
    {
        "code": "211",
        "segment": "3",
        "name": "CEDRAP",
        "time": "24H"
    },
    {
        "code": "212",
        "segment": "3",
        "name": "GASMIG",
        "time": "24H"
    },
    {
        "code": "216",
        "segment": "4",
        "name": "BRT MULTIMIDIA",
        "time": "24H"
    },
    {
        "code": "219",
        "segment": "5",
        "name": "SEFAZ-ES/DUA-DETRAN",
        "time": "24H"
    },
    {
        "code": "220",
        "segment": "3",
        "name": "CASTRO DISTRIBUICAO",
        "time": "24H"
    },
    {
        "code": "220",
        "segment": "4",
        "name": "OI S/A BR",
        "time": "24H"
    },
    {
        "code": "220",
        "segment": "5",
        "name": "DETRAN AM",
        "time": "24H"
    },
    {
        "code": "221",
        "segment": "3",
        "name": "CONSIGAZ",
        "time": "24H"
    },
    {
        "code": "221",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "222",
        "segment": "3",
        "name": "PROPANGAS",
        "time": "24H"
    },
    {
        "code": "223",
        "segment": "3",
        "name": "GASBALL",
        "time": "24H"
    },
    {
        "code": "223",
        "segment": "5",
        "name": "JUCEPE",
        "time": "24H"
    },
    {
        "code": "224",
        "segment": "5",
        "name": "SEFAZ-BA-FIES",
        "time": "24H"
    },
    {
        "code": "225",
        "segment": "5",
        "name": "SEFAZ-ES/DUA-HABILIT",
        "time": "20H"
    },
    {
        "code": "227",
        "segment": "3",
        "name": "NOVA FONTE ENERGIA",
        "time": "24H"
    },
    {
        "code": "229",
        "segment": "3",
        "name": "EBES ADM CONSORCIOS",
        "time": "24H"
    },
    {
        "code": "232",
        "segment": "3",
        "name": "COPA ENE",
        "time": "24H"
    },
    {
        "code": "233",
        "segment": "3",
        "name": "COBRAGEDI",
        "time": "24H"
    },
    {
        "code": "234",
        "segment": "3",
        "name": "GAS PONTO DISTR GAS",
        "time": "24H"
    },
    {
        "code": "236",
        "segment": "3",
        "name": "WE BRAZIL ENERGY",
        "time": "24H"
    },
    {
        "code": "253",
        "segment": "2",
        "name": "SAAE IGUATU",
        "time": "24H"
    },
    {
        "code": "253",
        "segment": "5",
        "name": "SEFAZ PB IPVA",
        "time": "24H"
    },
    {
        "code": "256",
        "segment": "5",
        "name": "PDJUD-ES",
        "time": "20H"
    },
    {
        "code": "260",
        "segment": "2",
        "name": "SAAE LIMOEIRO NORTE",
        "time": "24H"
    },
    {
        "code": "264",
        "segment": "5",
        "name": "SEFAZ PB FUNCEP DAR",
        "time": "24H"
    },
    {
        "code": "268",
        "segment": "5",
        "name": "SEFAZ-PI/ICMS",
        "time": "24H"
    },
    {
        "code": "268",
        "segment": "7",
        "name": "Prefeitura de Aracatuba Multas",
        "time": "24H"
    },
    {
        "code": "269",
        "segment": "2",
        "name": "SAAE SOBRAL",
        "time": "24H"
    },
    {
        "code": "273",
        "segment": "2",
        "name": "SAMAE IBIPORA",
        "time": "24H"
    },
    {
        "code": "279",
        "segment": "6",
        "name": "ASSOC MARIA REGINA C",
        "time": "24H"
    },
    {
        "code": "282",
        "segment": "6",
        "name": "ASSC N SRA GRACAS",
        "time": "24H"
    },
    {
        "code": "284",
        "segment": "4",
        "name": "ALGAR MULTIMIDIA",
        "time": "24H"
    },
    {
        "code": "285",
        "segment": "2",
        "name": "SAAE CERQUILHO",
        "time": "24H"
    },
    {
        "code": "285",
        "segment": "5",
        "name": "SEFAZ PB FFOFM TCE D",
        "time": "24H"
    },
    {
        "code": "286",
        "segment": "2",
        "name": "PARANAGUA SANEAMENTO",
        "time": "24H"
    },
    {
        "code": "290",
        "segment": "4",
        "name": "VIVO-PB",
        "time": "24H"
    },
    {
        "code": "291",
        "segment": "4",
        "name": "VIVO-AL",
        "time": "24H"
    },
    {
        "code": "292",
        "segment": "2",
        "name": "SAAEB-BEBEDOURO",
        "time": "24H"
    },
    {
        "code": "292",
        "segment": "4",
        "name": "VIVO-PE",
        "time": "24H"
    },
    {
        "code": "293",
        "segment": "4",
        "name": "VIVO-CE",
        "time": "24H"
    },
    {
        "code": "294",
        "segment": "4",
        "name": "VIVO-PI",
        "time": "24H"
    },
    {
        "code": "295",
        "segment": "4",
        "name": "VIVO-RN",
        "time": "24H"
    },
    {
        "code": "296",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "297",
        "segment": "2",
        "name": "SAAE VILHENA",
        "time": "24H"
    },
    {
        "code": "297",
        "segment": "4",
        "name": "CLARO S.A.",
        "time": "24H"
    },
    {
        "code": "304",
        "segment": "2",
        "name": "SEMAE SJRIO PRETO",
        "time": "24H"
    },
    {
        "code": "305",
        "segment": "2",
        "name": "SAAE SAO MATEUS",
        "time": "24H"
    },
    {
        "code": "305",
        "segment": "4",
        "name": "CLARO TV",
        "time": "24H"
    },
    {
        "code": "311",
        "segment": "2",
        "name": "DEMAE CALDAS NOVAS",
        "time": "24H"
    },
    {
        "code": "313",
        "segment": "4",
        "name": "OI MOVEL SUL CENTRO",
        "time": "24H"
    },
    {
        "code": "314",
        "segment": "2",
        "name": "SAAE SAO LOURENCO",
        "time": "24H"
    },
    {
        "code": "315",
        "segment": "2",
        "name": "SAAE IBITINGA",
        "time": "24H"
    },
    {
        "code": "318",
        "segment": "2",
        "name": "SAAE GOV VALADARES",
        "time": "24H"
    },
    {
        "code": "319",
        "segment": "2",
        "name": "CODEN-NOVA ODESSA",
        "time": "24H"
    },
    {
        "code": "320",
        "segment": "2",
        "name": "AGUAS DO IMPERADOR",
        "time": "24H"
    },
    {
        "code": "322",
        "segment": "2",
        "name": "AGUAS DE JUTURNAIBA",
        "time": "24H"
    },
    {
        "code": "324",
        "segment": "5",
        "name": "SEFAZ-RN-GRI",
        "time": "24H"
    },
    {
        "code": "325",
        "segment": "2",
        "name": "SAAE ABADIANIA",
        "time": "24H"
    },
    {
        "code": "326",
        "segment": "2",
        "name": "SAAE CORUMBA GOIAS",
        "time": "24H"
    },
    {
        "code": "330",
        "segment": "2",
        "name": "SEMASA CARANGOLA",
        "time": "24H"
    },
    {
        "code": "332",
        "segment": "2",
        "name": "SAAE AIMORES",
        "time": "24H"
    },
    {
        "code": "336",
        "segment": "2",
        "name": "SAAE MANHUACU",
        "time": "24H"
    },
    {
        "code": "337",
        "segment": "2",
        "name": "SAMAE CAXIAS DO SUL",
        "time": "24H"
    },
    {
        "code": "338",
        "segment": "2",
        "name": "SAAE SACRAMENTO",
        "time": "24H"
    },
    {
        "code": "341",
        "segment": "2",
        "name": "SANEAR RONDONOPOLIS",
        "time": "20H"
    },
    {
        "code": "348",
        "segment": "2",
        "name": "SAAE PIUMBI",
        "time": "24H"
    },
    {
        "code": "349",
        "segment": "2",
        "name": "DAEPA",
        "time": "24H"
    },
    {
        "code": "350",
        "segment": "2",
        "name": "SAMAE JAGUAPITA",
        "time": "24H"
    },
    {
        "code": "352",
        "segment": "2",
        "name": "SAAE BOA ESPERANCA",
        "time": "24H"
    },
    {
        "code": "353",
        "segment": "2",
        "name": "SAAE MACHADO",
        "time": "24H"
    },
    {
        "code": "354",
        "segment": "2",
        "name": "SAAE TRES PONTAS",
        "time": "24H"
    },
    {
        "code": "355",
        "segment": "2",
        "name": "SAAE ITAUNA",
        "time": "24H"
    },
    {
        "code": "355",
        "segment": "5",
        "name": "FMMAG GOIATUBA",
        "time": "24H"
    },
    {
        "code": "357",
        "segment": "2",
        "name": "SAMAE TIJUCAS",
        "time": "24H"
    },
    {
        "code": "361",
        "segment": "2",
        "name": "SAAE ITABIRITO",
        "time": "24H"
    },
    {
        "code": "362",
        "segment": "2",
        "name": "SAAE GUANHAES",
        "time": "24H"
    },
    {
        "code": "364",
        "segment": "2",
        "name": "NEPOMUCENO",
        "time": "24H"
    },
    {
        "code": "366",
        "segment": "2",
        "name": "SAAE OLIVEIRA",
        "time": "24H"
    },
    {
        "code": "369",
        "segment": "4",
        "name": "OI TV",
        "time": "24H"
    },
    {
        "code": "370",
        "segment": "2",
        "name": "PROLAGOS",
        "time": "20H"
    },
    {
        "code": "372",
        "segment": "2",
        "name": "SAAE BOCAIUVA",
        "time": "24H"
    },
    {
        "code": "375",
        "segment": "7",
        "name": "Prefeitura de Atibaia-Multas",
        "time": "24H"
    },
    {
        "code": "379",
        "segment": "4",
        "name": "SKY BRASIL",
        "time": "24H"
    },
    {
        "code": "380",
        "segment": "2",
        "name": "DMAES PONTE NOVA",
        "time": "24H"
    },
    {
        "code": "382",
        "segment": "2",
        "name": "DAE VARZEA GRANDE",
        "time": "24H"
    },
    {
        "code": "383",
        "segment": "2",
        "name": "SAAE SERTANOPOLIS",
        "time": "24H"
    },
    {
        "code": "384",
        "segment": "2",
        "name": "Prefeitura de Quatis-Agua",
        "time": "24H"
    },
    {
        "code": "389",
        "segment": "2",
        "name": "SAAE CAETE",
        "time": "24H"
    },
    {
        "code": "391",
        "segment": "2",
        "name": "AGUAS DO PARAIBA",
        "time": "24H"
    },
    {
        "code": "394",
        "segment": "2",
        "name": "DAMAE S J DEL REI",
        "time": "24H"
    },
    {
        "code": "397",
        "segment": "2",
        "name": "DMAE MONTE CARMELO",
        "time": "24H"
    },
    {
        "code": "398",
        "segment": "2",
        "name": "SAAE CONS PENA",
        "time": "24H"
    },
    {
        "code": "398",
        "segment": "6",
        "name": "ASSOC ARAUTOS",
        "time": "24H"
    },
    {
        "code": "399",
        "segment": "2",
        "name": "SAAE CAMBUI",
        "time": "24H"
    },
    {
        "code": "402",
        "segment": "2",
        "name": "DAE TUPACIGUARA",
        "time": "24H"
    },
    {
        "code": "402",
        "segment": "4",
        "name": "PORTO CONECTA",
        "time": "24H"
    },
    {
        "code": "403",
        "segment": "5",
        "name": "FMMA FEIRA SANTANA",
        "time": "24H"
    },
    {
        "code": "416",
        "segment": "4",
        "name": "TUBARON",
        "time": "24H"
    },
    {
        "code": "418",
        "segment": "2",
        "name": "DAE JOAO MONLEVADE",
        "time": "24H"
    },
    {
        "code": "423",
        "segment": "4",
        "name": "QNET",
        "time": "24H"
    },
    {
        "code": "424",
        "segment": "6",
        "name": "FDO MUN SAUDE SJOAOA",
        "time": "24H"
    },
    {
        "code": "425",
        "segment": "2",
        "name": "LOUVEIRA-AGUA",
        "time": "24H"
    },
    {
        "code": "426",
        "segment": "2",
        "name": "SAAE ITAPOLIS",
        "time": "24H"
    },
    {
        "code": "427",
        "segment": "2",
        "name": "SAAE PIRAPORA",
        "time": "24H"
    },
    {
        "code": "428",
        "segment": "5",
        "name": "GARE ICMS-PEP",
        "time": "24H"
    },
    {
        "code": "429",
        "segment": "4",
        "name": "WAVEMAX",
        "time": "24H"
    },
    {
        "code": "430",
        "segment": "4",
        "name": "HUGHESNET",
        "time": "24H"
    },
    {
        "code": "432",
        "segment": "5",
        "name": "DOC ARREC E-SOCIAL",
        "time": "24H"
    },
    {
        "code": "433",
        "segment": "2",
        "name": "SAAE MOEMA",
        "time": "24H"
    },
    {
        "code": "435",
        "segment": "2",
        "name": "SAAE CASIMIRO ABREU",
        "time": "24H"
    },
    {
        "code": "437",
        "segment": "4",
        "name": "ULTRAWAVE TELECOM",
        "time": "24H"
    },
    {
        "code": "440",
        "segment": "2",
        "name": "SAAE MAL.C RONDON",
        "time": "24H"
    },
    {
        "code": "440",
        "segment": "7",
        "name": "Prefeitura de Barbacena-Multas",
        "time": "24H"
    },
    {
        "code": "445",
        "segment": "2",
        "name": "LAGOA PRATA",
        "time": "24H"
    },
    {
        "code": "446",
        "segment": "2",
        "name": "CANF",
        "time": "24H"
    },
    {
        "code": "446",
        "segment": "4",
        "name": "PERSIS INTERNET",
        "time": "24H"
    },
    {
        "code": "449",
        "segment": "5",
        "name": "SEFAZ PB FUNDAGRO",
        "time": "24H"
    },
    {
        "code": "450",
        "segment": "2",
        "name": "SAAE CARMO DA MATA",
        "time": "24H"
    },
    {
        "code": "463",
        "segment": "2",
        "name": "Prefeitura de B Jesus Perdoes",
        "time": "24H"
    },
    {
        "code": "464",
        "segment": "4",
        "name": "ALGAR SOLUCOES",
        "time": "24H"
    },
    {
        "code": "465",
        "segment": "4",
        "name": "SKY BANDA LARGA",
        "time": "24H"
    },
    {
        "code": "467",
        "segment": "2",
        "name": "SANEAR COLATINA",
        "time": "24H"
    },
    {
        "code": "469",
        "segment": "4",
        "name": "VALENET",
        "time": "24H"
    },
    {
        "code": "470",
        "segment": "4",
        "name": "VOCE TELECOMUNICACOE",
        "time": "24H"
    },
    {
        "code": "473",
        "segment": "2",
        "name": "SAAE LAMBARI",
        "time": "24H"
    },
    {
        "code": "477",
        "segment": "2",
        "name": "AGUAS DE MANAUS",
        "time": "20H"
    },
    {
        "code": "478",
        "segment": "2",
        "name": "SAAE ITABIRA",
        "time": "24H"
    },
    {
        "code": "478",
        "segment": "4",
        "name": "SMART TELECOM",
        "time": "24H"
    },
    {
        "code": "479",
        "segment": "2",
        "name": "AGUAS DE NITEROI",
        "time": "24H"
    },
    {
        "code": "483",
        "segment": "2",
        "name": "SAS BARBACENA",
        "time": "24H"
    },
    {
        "code": "484",
        "segment": "5",
        "name": "SETEC CAMPINAS",
        "time": "24H"
    },
    {
        "code": "487",
        "segment": "4",
        "name": "PERSIS INTERNET",
        "time": "24H"
    },
    {
        "code": "488",
        "segment": "2",
        "name": "SAAEC CRATO",
        "time": "24H"
    },
    {
        "code": "488",
        "segment": "5",
        "name": "PROCON MACAE",
        "time": "24H"
    },
    {
        "code": "493",
        "segment": "4",
        "name": "TELEFONICA CLOUD",
        "time": "24H"
    },
    {
        "code": "496",
        "segment": "4",
        "name": "OI SOLUCOES S.A.",
        "time": "24H"
    },
    {
        "code": "497",
        "segment": "4",
        "name": "TELEFONICA IOT",
        "time": "24H"
    },
    {
        "code": "498",
        "segment": "2",
        "name": "SAAE PARINTINS",
        "time": "24H"
    },
    {
        "code": "504",
        "segment": "2",
        "name": "SAAE S FE SUL",
        "time": "24H"
    },
    {
        "code": "504",
        "segment": "4",
        "name": "VOGEL SOLUCOES TEL",
        "time": "24H"
    },
    {
        "code": "505",
        "segment": "4",
        "name": "TELEFONICA BRASIL",
        "time": "24H"
    },
    {
        "code": "507",
        "segment": "5",
        "name": "FMTT MACAE",
        "time": "24H"
    },
    {
        "code": "509",
        "segment": "4",
        "name": "DESAN TELECOM",
        "time": "24H"
    },
    {
        "code": "510",
        "segment": "4",
        "name": "BREM TECHNOLOGY",
        "time": "24H"
    },
    {
        "code": "512",
        "segment": "2",
        "name": "SAEMAP",
        "time": "24H"
    },
    {
        "code": "513",
        "segment": "2",
        "name": "DMAAE OURO FINO",
        "time": "24H"
    },
    {
        "code": "516",
        "segment": "2",
        "name": "SAAE ANGRA",
        "time": "24H"
    },
    {
        "code": "516",
        "segment": "4",
        "name": "SPIN TELECOMUNIC",
        "time": "24H"
    },
    {
        "code": "519",
        "segment": "5",
        "name": "Prefeitura de B Horizonte Ativo",
        "time": "24H"
    },
    {
        "code": "521",
        "segment": "7",
        "name": "FUNDO TRANS URBANOS",
        "time": "24H"
    },
    {
        "code": "527",
        "segment": "2",
        "name": "AGUAS DE SORRISO",
        "time": "24H"
    },
    {
        "code": "533",
        "segment": "2",
        "name": "SAMAE ARARANGUA",
        "time": "24H"
    },
    {
        "code": "534",
        "segment": "2",
        "name": "AGUAS GUARIROBA",
        "time": "20H"
    },
    {
        "code": "545",
        "segment": "7",
        "name": "Prefeitura de Betim-Multas",
        "time": "24H"
    },
    {
        "code": "554",
        "segment": "2",
        "name": "A.PEIXOTO AZEVEDO",
        "time": "24H"
    },
    {
        "code": "562",
        "segment": "5",
        "name": "FUMDEC TIMBO",
        "time": "24H"
    },
    {
        "code": "563",
        "segment": "5",
        "name": "FMMA TIMBO",
        "time": "24H"
    },
    {
        "code": "564",
        "segment": "5",
        "name": "FUMTRAN TIMBO",
        "time": "24H"
    },
    {
        "code": "567",
        "segment": "5",
        "name": "FME INDAIAL",
        "time": "24H"
    },
    {
        "code": "571",
        "segment": "5",
        "name": "FMS BARRO ALTO",
        "time": "24H"
    },
    {
        "code": "579",
        "segment": "5",
        "name": "FMS BELA VISTA GO",
        "time": "24H"
    },
    {
        "code": "580",
        "segment": "5",
        "name": "COVISA MACAE",
        "time": "24H"
    },
    {
        "code": "583",
        "segment": "5",
        "name": "BHPREV",
        "time": "24H"
    },
    {
        "code": "584",
        "segment": "5",
        "name": "FUFIN",
        "time": "24H"
    },
    {
        "code": "586",
        "segment": "5",
        "name": "FCJOL-F OSWALDO LIMA",
        "time": "24H"
    },
    {
        "code": "589",
        "segment": "5",
        "name": "BHTRANS",
        "time": "24H"
    },
    {
        "code": "605",
        "segment": "6",
        "name": "IPARV RIO VERDE",
        "time": "24H"
    },
    {
        "code": "607",
        "segment": "5",
        "name": "FMDDD TIMBO",
        "time": "24H"
    },
    {
        "code": "608",
        "segment": "5",
        "name": "FCT TIMBO",
        "time": "24H"
    },
    {
        "code": "614",
        "segment": "2",
        "name": "A PONTES E LACERDA",
        "time": "24H"
    },
    {
        "code": "622",
        "segment": "2",
        "name": "SANESSOL",
        "time": "24H"
    },
    {
        "code": "625",
        "segment": "2",
        "name": "DEMAE CAMPO BELO",
        "time": "24H"
    },
    {
        "code": "626",
        "segment": "2",
        "name": "COSMOPOLIS-CTA AGUA",
        "time": "24H"
    },
    {
        "code": "632",
        "segment": "2",
        "name": "DAP MUN CPO NOVO PAR",
        "time": "24H"
    },
    {
        "code": "635",
        "segment": "2",
        "name": "AGUAS DE SARANDI",
        "time": "24H"
    },
    {
        "code": "641",
        "segment": "2",
        "name": "SAAE S PEDRO TURVO",
        "time": "24H"
    },
    {
        "code": "646",
        "segment": "2",
        "name": "AGUAS CANARANA",
        "time": "24H"
    },
    {
        "code": "647",
        "segment": "5",
        "name": "SEFAZ RR PGEH",
        "time": "24H"
    },
    {
        "code": "653",
        "segment": "5",
        "name": "AMMA EUSEBIO CE",
        "time": "24H"
    },
    {
        "code": "657",
        "segment": "5",
        "name": "FMS TEIXEIRA FREITAS",
        "time": "24H"
    },
    {
        "code": "661",
        "segment": "2",
        "name": "SAAEB BROTAS",
        "time": "24H"
    },
    {
        "code": "670",
        "segment": "2",
        "name": "F.SERRA-GUAPIMIRIM",
        "time": "24H"
    },
    {
        "code": "678",
        "segment": "5",
        "name": "IMAS GOIANIA",
        "time": "24H"
    },
    {
        "code": "689",
        "segment": "2",
        "name": "SAAE B.J.ITABAPOANA",
        "time": "24H"
    },
    {
        "code": "693",
        "segment": "2",
        "name": "SAAE LAJINHA",
        "time": "24H"
    },
    {
        "code": "699",
        "segment": "2",
        "name": "DEAGUA SP",
        "time": "24H"
    },
    {
        "code": "704",
        "segment": "2",
        "name": "DAEP PENAPOLIS",
        "time": "24H"
    },
    {
        "code": "709",
        "segment": "2",
        "name": "SAE RANCHARIA",
        "time": "24H"
    },
    {
        "code": "710",
        "segment": "2",
        "name": "SAE CATALAO",
        "time": "24H"
    },
    {
        "code": "715",
        "segment": "2",
        "name": "AGUAS STA CARMEM",
        "time": "24H"
    },
    {
        "code": "721",
        "segment": "2",
        "name": "IPAUSSU-AGUA",
        "time": "24H"
    },
    {
        "code": "722",
        "segment": "2",
        "name": "Prefeitura de Est Gerbi Agua",
        "time": "24H"
    },
    {
        "code": "723",
        "segment": "2",
        "name": "JAGUARIUNA-AGUA",
        "time": "24H"
    },
    {
        "code": "725",
        "segment": "2",
        "name": "SAMOTRACIA",
        "time": "24H"
    },
    {
        "code": "736",
        "segment": "5",
        "name": "FMH FAZENDA RIO GRAN",
        "time": "24H"
    },
    {
        "code": "739",
        "segment": "2",
        "name": "SAEMAS-SERTAOZINHO",
        "time": "24H"
    },
    {
        "code": "751",
        "segment": "2",
        "name": "PMCASIMIROABREUAGUA",
        "time": "24H"
    },
    {
        "code": "755",
        "segment": "6",
        "name": "FUNDO SAUDE-LUZIANIA",
        "time": "24H"
    },
    {
        "code": "762",
        "segment": "2",
        "name": "AGUAS DE PRIMAVERA",
        "time": "20H"
    },
    {
        "code": "762",
        "segment": "5",
        "name": "FMMA TEXEIRA FREITAS",
        "time": "20H"
    },
    {
        "code": "766",
        "segment": "2",
        "name": "AGUAS COLIDER",
        "time": "24H"
    },
    {
        "code": "767",
        "segment": "5",
        "name": "FECON",
        "time": "24H"
    },
    {
        "code": "771",
        "segment": "2",
        "name": "SAAE APARECIDA",
        "time": "24H"
    },
    {
        "code": "772",
        "segment": "2",
        "name": "DMAEV-VICENTINOPOLIS",
        "time": "24H"
    },
    {
        "code": "774",
        "segment": "5",
        "name": "FMDCA BH",
        "time": "24H"
    },
    {
        "code": "775",
        "segment": "2",
        "name": "SEMAE PIRACEMA",
        "time": "24H"
    },
    {
        "code": "775",
        "segment": "5",
        "name": "FUMID BH",
        "time": "24H"
    },
    {
        "code": "780",
        "segment": "5",
        "name": "SEFAZ RR ANUNCIOS",
        "time": "24H"
    },
    {
        "code": "785",
        "segment": "2",
        "name": "A.NORTELANDIA",
        "time": "24H"
    },
    {
        "code": "789",
        "segment": "7",
        "name": "Prefeitura de Caieiras Multas",
        "time": "24H"
    },
    {
        "code": "790",
        "segment": "2",
        "name": "SAEEC ENG COELHO",
        "time": "24H"
    },
    {
        "code": "791",
        "segment": "5",
        "name": "FMS STO A DESCOBERTO",
        "time": "24H"
    },
    {
        "code": "793",
        "segment": "2",
        "name": "SAAE PARAISOPOLIS",
        "time": "24H"
    },
    {
        "code": "796",
        "segment": "5",
        "name": "FMPDC BELO HORIZONTE",
        "time": "24H"
    },
    {
        "code": "798",
        "segment": "2",
        "name": "CORSAN",
        "time": "24H"
    },
    {
        "code": "802",
        "segment": "2",
        "name": "AGUAS ALTA FLORESTA",
        "time": "24H"
    },
    {
        "code": "803",
        "segment": "2",
        "name": "SAAE PRATAPOLIS",
        "time": "24H"
    },
    {
        "code": "821",
        "segment": "5",
        "name": "Prefeitura de Vitoria P Geral",
        "time": "24H"
    },
    {
        "code": "822",
        "segment": "5",
        "name": "Prefeitura de Vitoria Semfa",
        "time": "24H"
    },
    {
        "code": "834",
        "segment": "2",
        "name": "SANTA ADELIA-AGUA",
        "time": "24H"
    },
    {
        "code": "842",
        "segment": "5",
        "name": "SEFAZ OB FSDS DAR",
        "time": "24H"
    },
    {
        "code": "843",
        "segment": "2",
        "name": "SEMASA-LAGES",
        "time": "24H"
    },
    {
        "code": "845",
        "segment": "2",
        "name": "SEMASA ITAJAI",
        "time": "24H"
    },
    {
        "code": "847",
        "segment": "2",
        "name": "SAMA",
        "time": "24H"
    },
    {
        "code": "848",
        "segment": "5",
        "name": "SEFAZ RR FEIT",
        "time": "24H"
    },
    {
        "code": "849",
        "segment": "2",
        "name": "Prefeitura de Descalvado-Semarh",
        "time": "24H"
    },
    {
        "code": "855",
        "segment": "2",
        "name": "SAAE TOMBOS",
        "time": "24H"
    },
    {
        "code": "867",
        "segment": "2",
        "name": "DAE QUERENCIA",
        "time": "24H"
    },
    {
        "code": "870",
        "segment": "2",
        "name": "A.MARCELANDIA",
        "time": "24H"
    },
    {
        "code": "883",
        "segment": "2",
        "name": "SAAE CRUZEIRO",
        "time": "24H"
    },
    {
        "code": "884",
        "segment": "5",
        "name": "FUNAP PARACAMBI",
        "time": "24H"
    },
    {
        "code": "885",
        "segment": "5",
        "name": "FMS TIMBO",
        "time": "24H"
    },
    {
        "code": "887",
        "segment": "2",
        "name": "SAN PEDRA PRETA",
        "time": "24H"
    },
    {
        "code": "907",
        "segment": "2",
        "name": "SEMAE RIO QUENTE",
        "time": "24H"
    },
    {
        "code": "908",
        "segment": "2",
        "name": "AGUAS DE VERA",
        "time": "24H"
    },
    {
        "code": "910",
        "segment": "2",
        "name": "CIA AGUAS DE ITAPEMA",
        "time": "24H"
    },
    {
        "code": "911",
        "segment": "2",
        "name": "SANEFRAI",
        "time": "24H"
    },
    {
        "code": "918",
        "segment": "2",
        "name": "SAAESP-SAO PEDRO",
        "time": "24H"
    },
    {
        "code": "919",
        "segment": "2",
        "name": "SAAE CRAVINHOS",
        "time": "24H"
    },
    {
        "code": "924",
        "segment": "6",
        "name": "DPVAT-LIDER",
        "time": "24H"
    },
    {
        "code": "933",
        "segment": "2",
        "name": "SAAE IPANEMA",
        "time": "24H"
    },
    {
        "code": "945",
        "segment": "2",
        "name": "SAAE MINEIROS",
        "time": "24H"
    },
    {
        "code": "950",
        "segment": "2",
        "name": "Prefeitura de Conchal",
        "time": "24H"
    },
    {
        "code": "952",
        "segment": "5",
        "name": "PROCON ITUMBIARA",
        "time": "24H"
    },
    {
        "code": "955",
        "segment": "5",
        "name": "FME TIMBO",
        "time": "24H"
    },
    {
        "code": "958",
        "segment": "5",
        "name": "FMMA BARRO ALTO",
        "time": "24H"
    },
    {
        "code": "961",
        "segment": "2",
        "name": "AGUAS DE JOINVILLE",
        "time": "24H"
    },
    {
        "code": "983",
        "segment": "5",
        "name": "ITUMBIARA-AMMAI",
        "time": "24H"
    },
    {
        "code": "993",
        "segment": "2",
        "name": "SESAN",
        "time": "24H"
    },
    {
        "code": "999",
        "segment": "5",
        "name": "AMT RIO VERDE",
        "time": "24H"
    },
    {
        "code": "1007",
        "segment": "2",
        "name": "AMAE-CACH MACACU",
        "time": "24H"
    },
    {
        "code": "1011",
        "segment": "2",
        "name": "PORTO INDIV ADM AGUA",
        "time": "24H"
    },
    {
        "code": "1027",
        "segment": "2",
        "name": "EMASA BALN CAMBORIU",
        "time": "24H"
    },
    {
        "code": "1029",
        "segment": "4",
        "name": "TELEFONICA SP",
        "time": "24H"
    },
    {
        "code": "1029",
        "segment": "6",
        "name": "SMT URUACU",
        "time": "24H"
    },
    {
        "code": "1031",
        "segment": "4",
        "name": "TELEFONICA IOT BIG D",
        "time": "24H"
    },
    {
        "code": "1032",
        "segment": "4",
        "name": "SAM TELECOMUNICACOES",
        "time": "24H"
    },
    {
        "code": "1034",
        "segment": "2",
        "name": "SAEAN ARTUR NOGUEIRA",
        "time": "24H"
    },
    {
        "code": "1041",
        "segment": "4",
        "name": "WAGNER R F INFORMATI",
        "time": "24H"
    },
    {
        "code": "1045",
        "segment": "2",
        "name": "Prefeitura de Cafelandia",
        "time": "24H"
    },
    {
        "code": "1066",
        "segment": "2",
        "name": "SAAE MARIANA",
        "time": "24H"
    },
    {
        "code": "1072",
        "segment": "2",
        "name": "SAEMBA BARIRI",
        "time": "24H"
    },
    {
        "code": "1085",
        "segment": "2",
        "name": "AGUAS GUARAMIRIM",
        "time": "24H"
    },
    {
        "code": "1098",
        "segment": "2",
        "name": "SAMAE PALHOCA",
        "time": "24H"
    },
    {
        "code": "1100",
        "segment": "2",
        "name": "CORSAN-PAC",
        "time": "24H"
    },
    {
        "code": "1103",
        "segment": "2",
        "name": "AGUAS COMODORO",
        "time": "24H"
    },
    {
        "code": "1106",
        "segment": "2",
        "name": "AGUAS N PROGRESSO",
        "time": "24H"
    },
    {
        "code": "1113",
        "segment": "2",
        "name": "AGUAS AGULHAS NEGRAS",
        "time": "24H"
    },
    {
        "code": "1116",
        "segment": "2",
        "name": "COPANOR",
        "time": "24H"
    },
    {
        "code": "1119",
        "segment": "2",
        "name": "ESAP PALESTINA",
        "time": "24H"
    },
    {
        "code": "1128",
        "segment": "2",
        "name": "COMUSA",
        "time": "24H"
    },
    {
        "code": "1138",
        "segment": "2",
        "name": "AGUAS DE POCONE",
        "time": "24H"
    },
    {
        "code": "1143",
        "segment": "2",
        "name": "Prefeitura de Itaju Agua",
        "time": "24H"
    },
    {
        "code": "1145",
        "segment": "2",
        "name": "AGUAS DE SAO JOSE",
        "time": "24H"
    },
    {
        "code": "1146",
        "segment": "2",
        "name": "Prefeitura de M Alegre Agua",
        "time": "24H"
    },
    {
        "code": "1148",
        "segment": "2",
        "name": "CASAN",
        "time": "24H"
    },
    {
        "code": "1175",
        "segment": "2",
        "name": "SANEPAR PARAGOMINAS",
        "time": "24H"
    },
    {
        "code": "1190",
        "segment": "7",
        "name": "Prefeitura de Congonhas",
        "time": "24H"
    },
    {
        "code": "1194",
        "segment": "7",
        "name": "Prefeitura de C Lafaiete-Multas",
        "time": "24H"
    },
    {
        "code": "1202",
        "segment": "2",
        "name": "DEST ENTRE RIOS-AGUA",
        "time": "24H"
    },
    {
        "code": "1207",
        "segment": "2",
        "name": "FOZ DO JAGUARIBE",
        "time": "24H"
    },
    {
        "code": "1217",
        "segment": "2",
        "name": "AGUAS DE ARACOIABA",
        "time": "24H"
    },
    {
        "code": "1231",
        "segment": "2",
        "name": "SEMAE OURO PRETO",
        "time": "24H"
    },
    {
        "code": "1241",
        "segment": "2",
        "name": "SAMAE ANTONINA",
        "time": "24H"
    },
    {
        "code": "1253",
        "segment": "2",
        "name": "AGUAS DE PIQUETE",
        "time": "24H"
    },
    {
        "code": "1263",
        "segment": "2",
        "name": "BRK STA GERTRUDES",
        "time": "24H"
    },
    {
        "code": "1264",
        "segment": "2",
        "name": "SAN MAIRINQUE",
        "time": "24H"
    },
    {
        "code": "1266",
        "segment": "2",
        "name": "SAAE ITUVERAVA",
        "time": "24H"
    },
    {
        "code": "1270",
        "segment": "2",
        "name": "AGUAS ANDRADINA",
        "time": "24H"
    },
    {
        "code": "1271",
        "segment": "2",
        "name": "COLORADO-AGUA",
        "time": "24H"
    },
    {
        "code": "1278",
        "segment": "2",
        "name": "SAMASA TRES BARRAS",
        "time": "24H"
    },
    {
        "code": "1280",
        "segment": "2",
        "name": "AGUAS DE CASTILHO",
        "time": "24H"
    },
    {
        "code": "1292",
        "segment": "2",
        "name": "CEDAE",
        "time": "24H"
    },
    {
        "code": "1293",
        "segment": "2",
        "name": "CEDAE",
        "time": "24H"
    },
    {
        "code": "1295",
        "segment": "2",
        "name": "AGUAS DE PALHOCA",
        "time": "24H"
    },
    {
        "code": "1304",
        "segment": "2",
        "name": "SAMAE BLUMENAU",
        "time": "24H"
    },
    {
        "code": "1310",
        "segment": "2",
        "name": "BRK URUGUAIANA",
        "time": "24H"
    },
    {
        "code": "1316",
        "segment": "2",
        "name": "SAAE PEDREIRA",
        "time": "24H"
    },
    {
        "code": "1318",
        "segment": "2",
        "name": "BRK PORTO FERREIRA",
        "time": "24H"
    },
    {
        "code": "1324",
        "segment": "2",
        "name": "SISAM MACATUBA",
        "time": "24H"
    },
    {
        "code": "1329",
        "segment": "2",
        "name": "CAB CUIABA",
        "time": "24H"
    },
    {
        "code": "1330",
        "segment": "2",
        "name": "TUBARAO SANEAMENTO",
        "time": "24H"
    },
    {
        "code": "1333",
        "segment": "2",
        "name": "FOZ ZONA OESTE",
        "time": "24H"
    },
    {
        "code": "1335",
        "segment": "2",
        "name": "AGUAS DE VOTORANTIM",
        "time": "24H"
    },
    {
        "code": "1341",
        "segment": "2",
        "name": "ATS AG TOCANTINENSE",
        "time": "24H"
    },
    {
        "code": "1345",
        "segment": "2",
        "name": "SAMAR ARACATUBA",
        "time": "24H"
    },
    {
        "code": "1346",
        "segment": "2",
        "name": "BRK ARAGUAIA",
        "time": "24H"
    },
    {
        "code": "1347",
        "segment": "2",
        "name": "ITAPOA SANEAMENTO",
        "time": "24H"
    },
    {
        "code": "1349",
        "segment": "2",
        "name": "BRK MACAE",
        "time": "24H"
    },
    {
        "code": "1358",
        "segment": "2",
        "name": "A.PORTO ESPERIDIAO",
        "time": "24H"
    },
    {
        "code": "1365",
        "segment": "2",
        "name": "SAEMA MARIALVA",
        "time": "24H"
    },
    {
        "code": "1376",
        "segment": "2",
        "name": "CORREGO B.JESUS-AGUA",
        "time": "24H"
    },
    {
        "code": "1376",
        "segment": "7",
        "name": "DIVINOPOLIS MULTAS",
        "time": "24H"
    },
    {
        "code": "1379",
        "segment": "2",
        "name": "BRK GOIAS",
        "time": "24H"
    },
    {
        "code": "1385",
        "segment": "2",
        "name": "SAAE CORDEIROPOLIS",
        "time": "24H"
    },
    {
        "code": "1387",
        "segment": "2",
        "name": "AGUAS DE MATAO",
        "time": "24H"
    },
    {
        "code": "1388",
        "segment": "2",
        "name": "AGUAS DE CONFRESA",
        "time": "24H"
    },
    {
        "code": "1389",
        "segment": "2",
        "name": "SAAE SOLEDADE MINAS",
        "time": "24H"
    },
    {
        "code": "1393",
        "segment": "2",
        "name": "AGUAS SAO FRANCISCO",
        "time": "20H"
    },
    {
        "code": "1398",
        "segment": "2",
        "name": "IMBITUBA-CTA AGUA",
        "time": "24H"
    },
    {
        "code": "1399",
        "segment": "2",
        "name": "SAMAE TERRA RICA",
        "time": "24H"
    },
    {
        "code": "1402",
        "segment": "2",
        "name": "AGUAS DE PARATY",
        "time": "24H"
    },
    {
        "code": "1413",
        "segment": "2",
        "name": "AGUAS BARRA GARCA",
        "time": "20H"
    },
    {
        "code": "1422",
        "segment": "2",
        "name": "AGUAS DE SINOP",
        "time": "20H"
    },
    {
        "code": "1423",
        "segment": "2",
        "name": "AGUAS DE JAHU",
        "time": "24H"
    },
    {
        "code": "1426",
        "segment": "2",
        "name": "AGUAS S FRANCISO SUL",
        "time": "24H"
    },
    {
        "code": "1429",
        "segment": "2",
        "name": "BRK MARANHAO",
        "time": "24H"
    },
    {
        "code": "1432",
        "segment": "2",
        "name": "AGUAS PARANATINGA",
        "time": "24H"
    },
    {
        "code": "1436",
        "segment": "2",
        "name": "BRK SUMARE",
        "time": "24H"
    },
    {
        "code": "1442",
        "segment": "2",
        "name": "AGUAS PARA DE MINAS",
        "time": "24H"
    },
    {
        "code": "1443",
        "segment": "2",
        "name": "AGUAS DE TIMON",
        "time": "20H"
    },
    {
        "code": "1447",
        "segment": "2",
        "name": "SANESALTO",
        "time": "24H"
    },
    {
        "code": "1452",
        "segment": "6",
        "name": "A.VIRACOPOS",
        "time": "24H"
    },
    {
        "code": "1456",
        "segment": "2",
        "name": "CAEPA",
        "time": "24H"
    },
    {
        "code": "1459",
        "segment": "2",
        "name": "AGUAS DE MERITI",
        "time": "24H"
    },
    {
        "code": "1462",
        "segment": "2",
        "name": "AGUA DE HOLAMBRA",
        "time": "24H"
    },
    {
        "code": "1466",
        "segment": "2",
        "name": "AGUAS DE PENHA",
        "time": "24H"
    },
    {
        "code": "1472",
        "segment": "2",
        "name": "Prefeitura de Ipiacu-Agua",
        "time": "24H"
    },
    {
        "code": "1473",
        "segment": "2",
        "name": "AGUAS CAMBORIU",
        "time": "20H"
    },
    {
        "code": "1476",
        "segment": "2",
        "name": "AGUAS DO PANTANAL",
        "time": "24H"
    },
    {
        "code": "1484",
        "segment": "2",
        "name": "COMASA",
        "time": "24H"
    },
    {
        "code": "1491",
        "segment": "2",
        "name": "A.ROLIM MOURA",
        "time": "20H"
    },
    {
        "code": "1493",
        "segment": "2",
        "name": "AGUAS DE ARIQUEMES",
        "time": "20H"
    },
    {
        "code": "1494",
        "segment": "2",
        "name": "EPPO AGUAS",
        "time": "24H"
    },
    {
        "code": "1499",
        "segment": "2",
        "name": "AGUAS DE BOMBINHAS",
        "time": "20H"
    },
    {
        "code": "1507",
        "segment": "2",
        "name": "AGUA Prefeitura de Sjv Rio Pret",
        "time": "24H"
    },
    {
        "code": "1508",
        "segment": "2",
        "name": "AGUA Prefeitura de Pontal",
        "time": "24H"
    },
    {
        "code": "1514",
        "segment": "2",
        "name": "PREF MUN PRES VENCESLAU-DAE ",
        "time": "24H"
    },
    {
        "code": "1515",
        "segment": "2",
        "name": "SAAE CARMESIA",
        "time": "24H"
    },
    {
        "code": "1520",
        "segment": "2",
        "name": "CIS ITUANA",
        "time": "24H"
    },
    {
        "code": "1535",
        "segment": "2",
        "name": "AGUAS TERESINA",
        "time": "20H"
    },
    {
        "code": "1537",
        "segment": "2",
        "name": "ITEBRA",
        "time": "24H"
    },
    {
        "code": "1550",
        "segment": "2",
        "name": "EMBASA",
        "time": "24H"
    },
    {
        "code": "1551",
        "segment": "2",
        "name": "EMBASA",
        "time": "24H"
    },
    {
        "code": "1553",
        "segment": "2",
        "name": "Prefeitura de Lindoia",
        "time": "24H"
    },
    {
        "code": "1557",
        "segment": "6",
        "name": "A.GUARULHOS",
        "time": "24H"
    },
    {
        "code": "1562",
        "segment": "7",
        "name": "MULTAS FERRAZ VASCON",
        "time": "24H"
    },
    {
        "code": "1585",
        "segment": "2",
        "name": "Prefeitura de Pitangueiras",
        "time": "24H"
    },
    {
        "code": "1603",
        "segment": "2",
        "name": "Prefeitura de Serrana-Daes",
        "time": "24H"
    },
    {
        "code": "1612",
        "segment": "2",
        "name": "VISAN VIDEIRA SANEAM",
        "time": "24H"
    },
    {
        "code": "1619",
        "segment": "2",
        "name": "BRK CACADOR",
        "time": "24H"
    },
    {
        "code": "1639",
        "segment": "2",
        "name": "SAAE POCRANE",
        "time": "24H"
    },
    {
        "code": "1645",
        "segment": "2",
        "name": "Prefeitura de Jeceaba Agua",
        "time": "24H"
    },
    {
        "code": "1655",
        "segment": "2",
        "name": "ANE AGUAS DO NORDEST",
        "time": "24H"
    },
    {
        "code": "1658",
        "segment": "2",
        "name": "SANEOURO",
        "time": "24H"
    },
    {
        "code": "1671",
        "segment": "2",
        "name": "BRK MACEIO",
        "time": "24H"
    },
    {
        "code": "1679",
        "segment": "2",
        "name": "AGUAS DA CONDESSA",
        "time": "24H"
    },
    {
        "code": "1684",
        "segment": "2",
        "name": "SAMAE JAGUARIAIVA",
        "time": "24H"
    },
    {
        "code": "1688",
        "segment": "2",
        "name": "SANEL",
        "time": "24H"
    },
    {
        "code": "1698",
        "segment": "2",
        "name": "AGUAS DO RIO",
        "time": "24H"
    },
    {
        "code": "1699",
        "segment": "2",
        "name": "AGUAS DO RIO",
        "time": "24H"
    },
    {
        "code": "1703",
        "segment": "7",
        "name": "Prefeitura de Gov Valadarese Mu",
        "time": "24H"
    },
    {
        "code": "1712",
        "segment": "2",
        "name": "IGUA RIO DE JANEIRO",
        "time": "24H"
    },
    {
        "code": "1713",
        "segment": "2",
        "name": "IGUA RIO DE JANEIRO",
        "time": "24H"
    },
    {
        "code": "1714",
        "segment": "2",
        "name": "IGUA RIO DE JANEIRO",
        "time": "24H"
    },
    {
        "code": "1717",
        "segment": "6",
        "name": "COHAB-MG",
        "time": "24H"
    },
    {
        "code": "1725",
        "segment": "2",
        "name": "AMBIENTAL CRATO",
        "time": "24H"
    },
    {
        "code": "1726",
        "segment": "2",
        "name": "RIO MAIS SANEAMENTO",
        "time": "24H"
    },
    {
        "code": "1728",
        "segment": "2",
        "name": "VERDE AMB AL",
        "time": "24H"
    },
    {
        "code": "1731",
        "segment": "2",
        "name": "SANOR ORLANDIA",
        "time": "24H"
    },
    {
        "code": "1733",
        "segment": "2",
        "name": "AGUAS IPAMERI",
        "time": "24H"
    },
    {
        "code": "1741",
        "segment": "2",
        "name": "EPAC SANEAMENTO BASI",
        "time": "24H"
    },
    {
        "code": "1770",
        "segment": "7",
        "name": "Prefeitura de Guararema-Multas",
        "time": "24H"
    },
    {
        "code": "1810",
        "segment": "7",
        "name": "Prefeitura de Hortolandia Multa",
        "time": "24H"
    },
    {
        "code": "1859",
        "segment": "7",
        "name": "Prefeitura de Ibirite Multas",
        "time": "24H"
    },
    {
        "code": "1953",
        "segment": "7",
        "name": "IPATINGA MULTAS",
        "time": "24H"
    },
    {
        "code": "1967",
        "segment": "6",
        "name": "A.CONFINS",
        "time": "24H"
    },
    {
        "code": "1972",
        "segment": "6",
        "name": "A. GALEAO",
        "time": "24H"
    },
    {
        "code": "2012",
        "segment": "7",
        "name": "PMITABIRA",
        "time": "24H"
    },
    {
        "code": "2048",
        "segment": "7",
        "name": "ITAJUBA-MULTA",
        "time": "24H"
    },
    {
        "code": "2080",
        "segment": "7",
        "name": "Prefeitura de Itapecerica Multa",
        "time": "24H"
    },
    {
        "code": "2091",
        "segment": "7",
        "name": "Prefeitura de Itapevi Multa",
        "time": "24H"
    },
    {
        "code": "2126",
        "segment": "7",
        "name": "ITATIBA-MULTAS",
        "time": "24H"
    },
    {
        "code": "2319",
        "segment": "7",
        "name": "PMJUNDIAI MULTA",
        "time": "24H"
    },
    {
        "code": "2431",
        "segment": "7",
        "name": "Prefeitura de Limeira-Multa",
        "time": "24H"
    },
    {
        "code": "2462",
        "segment": "6",
        "name": "PAG LOGISTICA",
        "time": "24H"
    },
    {
        "code": "2499",
        "segment": "2",
        "name": "SAAE SETE LAGOAS",
        "time": "24H"
    },
    {
        "code": "2506",
        "segment": "7",
        "name": "Prefeitura de Mairipora-Multas",
        "time": "24H"
    },
    {
        "code": "2581",
        "segment": "7",
        "name": "Prefeitura de Mariana-Multas",
        "time": "24H"
    },
    {
        "code": "2705",
        "segment": "6",
        "name": "AEROPORTO FOR/POA",
        "time": "24H"
    },
    {
        "code": "2784",
        "segment": "6",
        "name": "AER HERCILIO LUZ",
        "time": "24H"
    },
    {
        "code": "2795",
        "segment": "6",
        "name": "AER SALVADOR",
        "time": "24H"
    },
    {
        "code": "3011",
        "segment": "7",
        "name": "Prefeitura de Osasco Multa",
        "time": "24H"
    },
    {
        "code": "3014",
        "segment": "7",
        "name": "Prefeitura de O Cruz Multas",
        "time": "24H"
    },
    {
        "code": "3127",
        "segment": "2",
        "name": "BRK MAUA",
        "time": "24H"
    },
    {
        "code": "3173",
        "segment": "7",
        "name": "Prefeitura de Patrocinio-Multa",
        "time": "24H"
    },
    {
        "code": "3228",
        "segment": "6",
        "name": "PORTO SECO PONTA NEG",
        "time": "24H"
    },
    {
        "code": "3350",
        "segment": "7",
        "name": "Prefeitura de Pirassununga Mult",
        "time": "24H"
    },
    {
        "code": "3362",
        "segment": "6",
        "name": "DPVAT",
        "time": "24H"
    },
    {
        "code": "3394",
        "segment": "7",
        "name": "POCOS CALDA MULTA",
        "time": "24H"
    },
    {
        "code": "3415",
        "segment": "7",
        "name": "Prefeitura de Ponte Nova-Multa",
        "time": "24H"
    },
    {
        "code": "3466",
        "segment": "7",
        "name": "POUSO ALEGRE-MULTA",
        "time": "24H"
    },
    {
        "code": "3475",
        "segment": "7",
        "name": "SETRAN PRAIA GRANDE",
        "time": "24H"
    },
    {
        "code": "3627",
        "segment": "7",
        "name": "Prefeitura de Rib Neves-Multas",
        "time": "24H"
    },
    {
        "code": "3659",
        "segment": "7",
        "name": "Prefeitura de Rio Janeiro Multa",
        "time": "24H"
    },
    {
        "code": "3738",
        "segment": "7",
        "name": "Prefeitura de Sabara Multas",
        "time": "24H"
    },
    {
        "code": "3742",
        "segment": "2",
        "name": "SANESC",
        "time": "24H"
    },
    {
        "code": "3776",
        "segment": "7",
        "name": "TRANSALVADOR",
        "time": "24H"
    },
    {
        "code": "3846",
        "segment": "7",
        "name": "MULTA Prefeitura de S Luzia",
        "time": "24H"
    },
    {
        "code": "3847",
        "segment": "2",
        "name": "BRK MAUA",
        "time": "24H"
    },
    {
        "code": "3884",
        "segment": "7",
        "name": "Prefeitura de S Rita Sapucai Mu",
        "time": "24H"
    },
    {
        "code": "4158",
        "segment": "7",
        "name": "Prefeitura de S Jose Multas",
        "time": "24H"
    },
    {
        "code": "4213",
        "segment": "6",
        "name": "CCR BLOCO SUL",
        "time": "24H"
    },
    {
        "code": "4220",
        "segment": "6",
        "name": "CCR AEROPORTOS BL CE",
        "time": "24H"
    },
    {
        "code": "4254",
        "segment": "6",
        "name": "AEROPORTOS AMAZONIA",
        "time": "24H"
    },
    {
        "code": "4404",
        "segment": "7",
        "name": "MULTA Prefeitura de Sorocaba",
        "time": "24H"
    },
    {
        "code": "4414",
        "segment": "7",
        "name": "Prefeitura de Sumare Multas",
        "time": "24H"
    },
    {
        "code": "4424",
        "segment": "7",
        "name": "Prefeitura de Taboao Multas",
        "time": "24H"
    },
    {
        "code": "4510",
        "segment": "7",
        "name": "Prefeitura de T.Otoni-Multa",
        "time": "24H"
    },
    {
        "code": "4544",
        "segment": "7",
        "name": "Prefeitura de Tiradentes Multas",
        "time": "24H"
    },
    {
        "code": "4573",
        "segment": "7",
        "name": "Prefeitura de Tres Coracoes-Mul",
        "time": "24H"
    },
    {
        "code": "4581",
        "segment": "7",
        "name": "TRES PONTAS-MULTAS",
        "time": "24H"
    },
    {
        "code": "4630",
        "segment": "7",
        "name": "UBA MULTAS DE TRANSI",
        "time": "24H"
    },
    {
        "code": "4641",
        "segment": "6",
        "name": "AEROPORTO S JOSE CPO",
        "time": "24H"
    },
    {
        "code": "4733",
        "segment": "2",
        "name": "SABESP OLIMPIA",
        "time": "24H"
    },
    {
        "code": "4750",
        "segment": "7",
        "name": "Prefeitura de Vicosa-Multa",
        "time": "24H"
    },
    {
        "code": "5827",
        "segment": "7",
        "name": "MULTA ESTADUAL MG",
        "time": "24H"
    },
    {
        "code": "5828",
        "segment": "7",
        "name": "MULTA DER MG",
        "time": "24H"
    },
    {
        "code": "6075",
        "segment": "6",
        "name": "SOC FAMILIA PROPRIED",
        "time": "24H"
    },
    {
        "code": "7864",
        "segment": "6",
        "name": "UEL",
        "time": "24H"
    },
]
