import json
import time
import requests

sch_list = [
  {
    "sekolah_id": 1005768,
    "siap_id": False,
    "nama": "SMK NEGERI 1",
    "npsn": 20100143,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005769,
    "siap_id": False,
    "nama": "SMK NEGERI 2",
    "npsn": 20100161,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005770,
    "siap_id": False,
    "nama": "SMK NEGERI 3",
    "npsn": 20100164,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005771,
    "siap_id": False,
    "nama": "SMK NEGERI 4",
    "npsn": 20107436,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005772,
    "siap_id": False,
    "nama": "SMK NEGERI 5",
    "npsn": 20103783,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005773,
    "siap_id": False,
    "nama": "SMK NEGERI 6",
    "npsn": 20102579,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005774,
    "siap_id": False,
    "nama": "SMK NEGERI 7",
    "npsn": 20103778,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005775,
    "siap_id": False,
    "nama": "SMK NEGERI 8",
    "npsn": 20102597,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005776,
    "siap_id": False,
    "nama": "SMK NEGERI 9",
    "npsn": 20101496,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005777,
    "siap_id": False,
    "nama": "SMK NEGERI 10",
    "npsn": 20103791,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005778,
    "siap_id": False,
    "nama": "SMK NEGERI 11",
    "npsn": 20101504,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005779,
    "siap_id": False,
    "nama": "SMK NEGERI 12",
    "npsn": 20100783,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005780,
    "siap_id": False,
    "nama": "SMK NEGERI 13",
    "npsn": 20101503,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005781,
    "siap_id": False,
    "nama": "SMK NEGERI 14",
    "npsn": 20100158,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005782,
    "siap_id": False,
    "nama": "SMK NEGERI 15",
    "npsn": 20102578,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005783,
    "siap_id": False,
    "nama": "SMK NEGERI 16",
    "npsn": 20100159,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005784,
    "siap_id": False,
    "nama": "SMK NEGERI 17",
    "npsn": 20101502,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005785,
    "siap_id": False,
    "nama": "SMK NEGERI 18",
    "npsn": 20102589,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005786,
    "siap_id": False,
    "nama": "SMK NEGERI 19",
    "npsn": 20100160,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005787,
    "siap_id": False,
    "nama": "SMK NEGERI 20",
    "npsn": 20102587,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005788,
    "siap_id": False,
    "nama": "SMK NEGERI 21",
    "npsn": 20100162,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005789,
    "siap_id": False,
    "nama": "SMK NEGERI 22",
    "npsn": 20103790,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005790,
    "siap_id": False,
    "nama": "SMK NEGERI 23",
    "npsn": 20107433,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005791,
    "siap_id": False,
    "nama": "SMK NEGERI 24",
    "npsn": 20103788,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005792,
    "siap_id": False,
    "nama": "SMK NEGERI 25",
    "npsn": 20102586,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005793,
    "siap_id": False,
    "nama": "SMK NEGERI 26",
    "npsn": 20103787,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005794,
    "siap_id": False,
    "nama": "SMK NEGERI 27",
    "npsn": 20100163,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005795,
    "siap_id": False,
    "nama": "SMK NEGERI 28",
    "npsn": 20102585,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005796,
    "siap_id": False,
    "nama": "SMK NEGERI 29",
    "npsn": 20102602,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005797,
    "siap_id": False,
    "nama": "SMK NEGERI 30",
    "npsn": 20102582,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005798,
    "siap_id": False,
    "nama": "SMK NEGERI 31",
    "npsn": 20100165,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005799,
    "siap_id": False,
    "nama": "SMK NEGERI 32",
    "npsn": 20102581,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005800,
    "siap_id": False,
    "nama": "SMK NEGERI 33",
    "npsn": 20107434,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005801,
    "siap_id": False,
    "nama": "SMK NEGERI 34",
    "npsn": 20100166,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005802,
    "siap_id": False,
    "nama": "SMK NEGERI 35",
    "npsn": 20101501,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005803,
    "siap_id": False,
    "nama": "SMK NEGERI 36",
    "npsn": 20107435,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005804,
    "siap_id": False,
    "nama": "SMK NEGERI 37",
    "npsn": 20102601,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005805,
    "siap_id": False,
    "nama": "SMK NEGERI 38",
    "npsn": 20100167,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005806,
    "siap_id": False,
    "nama": "SMK NEGERI 39",
    "npsn": 20100168,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005807,
    "siap_id": False,
    "nama": "SMK NEGERI 40",
    "npsn": 20103786,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005808,
    "siap_id": False,
    "nama": "SMK NEGERI 41",
    "npsn": 20102580,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005809,
    "siap_id": False,
    "nama": "SMK NEGERI 42",
    "npsn": 20101500,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005810,
    "siap_id": False,
    "nama": "SMK NEGERI 43",
    "npsn": 20102600,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005811,
    "siap_id": False,
    "nama": "SMK NEGERI 44",
    "npsn": 20100157,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005812,
    "siap_id": False,
    "nama": "SMK NEGERI 45",
    "npsn": 20101499,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005813,
    "siap_id": False,
    "nama": "SMK NEGERI 46",
    "npsn": 20103785,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005814,
    "siap_id": False,
    "nama": "SMK NEGERI 47",
    "npsn": 20102599,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005815,
    "siap_id": False,
    "nama": "SMK NEGERI 48",
    "npsn": 20103784,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005816,
    "siap_id": False,
    "nama": "SMK NEGERI 49",
    "npsn": 20107437,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005817,
    "siap_id": False,
    "nama": "SMK NEGERI 50",
    "npsn": 20103782,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005818,
    "siap_id": False,
    "nama": "SMK NEGERI 51",
    "npsn": 20103781,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005819,
    "siap_id": False,
    "nama": "SMK NEGERI 52",
    "npsn": 20103780,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005820,
    "siap_id": False,
    "nama": "SMK NEGERI 53",
    "npsn": 20101498,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005821,
    "siap_id": False,
    "nama": "SMK NEGERI 54",
    "npsn": 20100156,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20102,
    "k_propinsi": 201,
    "kota": "Jakarta Pusat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005822,
    "siap_id": False,
    "nama": "SMK NEGERI 55",
    "npsn": 20107438,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005823,
    "siap_id": False,
    "nama": "SMK NEGERI 56",
    "npsn": 20107439,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20103,
    "k_propinsi": 201,
    "kota": "Jakarta Utara",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005824,
    "siap_id": False,
    "nama": "SMK NEGERI 57",
    "npsn": 20102598,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005825,
    "siap_id": False,
    "nama": "SMK NEGERI 58",
    "npsn": 20103779,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005826,
    "siap_id": False,
    "nama": "SMK NEGERI 59",
    "npsn": 20107358,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005827,
    "siap_id": False,
    "nama": "SMK NEGERI 60",
    "npsn": 20101497,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005828,
    "siap_id": False,
    "nama": "SMK NEGERI 61 (KEPULAUAN SERIBU)",
    "npsn": 20109165,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20101,
    "k_propinsi": 201,
    "kota": "Kepulauan Seribu",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005829,
    "siap_id": False,
    "nama": "SMK NEGERI 62",
    "npsn": 20109246,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005830,
    "siap_id": False,
    "nama": "SMK NEGERI 63",
    "npsn": 20112443,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005831,
    "siap_id": False,
    "nama": "SMK NEGERI 64",
    "npsn": 69992315,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005832,
    "siap_id": False,
    "nama": "SMK NEGERI 65",
    "npsn": 69992316,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005833,
    "siap_id": False,
    "nama": "SMK NEGERI 66",
    "npsn": 69992317,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005834,
    "siap_id": False,
    "nama": "SMK NEGERI 67",
    "npsn": 69992318,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005835,
    "siap_id": False,
    "nama": "SMK NEGERI 68",
    "npsn": 69992319,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005836,
    "siap_id": False,
    "nama": "SMK NEGERI 69",
    "npsn": 69992321,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005837,
    "siap_id": False,
    "nama": "SMK NEGERI 70",
    "npsn": 69992314,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005838,
    "siap_id": False,
    "nama": "SMK NEGERI 71",
    "npsn": 69992322,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20106,
    "k_propinsi": 201,
    "kota": "Jakarta Timur",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005839,
    "siap_id": False,
    "nama": "SMK NEGERI 72",
    "npsn": 69992346,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005840,
    "siap_id": False,
    "nama": "SMK NEGERI 73",
    "npsn": 69992323,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20104,
    "k_propinsi": 201,
    "kota": "Jakarta Barat",
    "propinsi": "DKI Jakarta",
    "logo": ""
  },
  {
    "sekolah_id": 1005841,
    "siap_id": False,
    "nama": "SMK NEGERI 74",
    "npsn": 70054389,
    "is_negeri": True,
    "is_sbi": False,
    "k_kota": 20105,
    "k_propinsi": 201,
    "kota": "Jakarta Selatan",
    "propinsi": "DKI Jakarta",
    "logo": ""
  }
]

sch_detail_list = {
  "1005768": {
    "sekolah": "SMK NEGERI 1",
    "kompetensi": [
      "Teknik Konstruksi dan Perumahan",
      "Desain Gambar Mesin",
      "Desain Pemodelan dan Informasi Bangunan",
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Rekayasa Perangkat Lunak",
      "Teknik Komputer dan Jaringan",
      "Sistem Informasi, Jaringan dan Aplikasi",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [
      1857, 1861, 1858, 1859, 1860, 1862, 1863, 1865, 1864, 1866
    ],
    "kapasitas": [
      [[26, 0, 46]],
      [[13, 0, 46]],
      [[26, 0, 46]],
      [[38, 0, 46]],
      [[25, 0, 46]],
      [[25, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["46.05", "49.17", "46.75"],
      ["46.08", "49.04", "46.78"],
      ["46.30", "50.60", "47.42"],
      ["46.24", "50.61", "47.41"],
      ["46.86", "51.85", "48.01"],
      ["47.03", "51.27", "47.94"],
      ["48.17", "52.91", "49.94"],
      ["48.80", "52.80", "50.30"],
      ["47.99", "54.03", "50.10"],
      ["48.70", "54.83", "50.58"]
    ],
    "peminat": [
      { "1": [65, 0, 185], "2": [30, 0, 139], "3": [27, 0, 120] },
      { "1": [32, 0, 185], "2": [20, 0, 139], "3": [16, 0, 120] },
      { "1": [47, 0, 185], "2": [21, 0, 139], "3": [16, 0, 120] },
      { "1": [94, 0, 185], "2": [45, 0, 139], "3": [41, 0, 120] },
      { "1": [82, 0, 185], "2": [54, 0, 139], "3": [37, 0, 120] },
      { "1": [148, 0, 185], "2": [58, 0, 139], "3": [67, 0, 120] },
      { "1": [42, 0, 185], "2": [22, 0, 139], "3": [13, 0, 120] },
      { "1": [85, 0, 185], "2": [39, 0, 139], "3": [34, 0, 120] },
      { "1": [35, 0, 185], "2": [13, 0, 139], "3": [15, 0, 120] },
      { "1": [53, 0, 185], "2": [26, 0, 139], "3": [32, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [31, 0, 43], "2": [4, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [25, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005769": {
    "sekolah": "SMK NEGERI 2",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1867, 1868, 1869, 1870, 1871],
    "kapasitas": [
      [[25, 0, 46]],
      [[27, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[10, 0, 46]]
    ],
    "rekap": [
      ["46.56", "50.40", "47.99"],
      ["46.59", "50.75", "47.86"],
      ["49.28", "52.79", "50.72"],
      ["47.47", "54.54", "49.21"],
      ["48.30", "50.26", "49.20"]
    ],
    "peminat": [
      { "1": [35, 0, 185], "2": [36, 0, 139], "3": [20, 0, 120] },
      { "1": [49, 0, 185], "2": [38, 0, 139], "3": [27, 0, 120] },
      { "1": [62, 0, 185], "2": [39, 0, 139], "3": [26, 0, 120] },
      { "1": [23, 0, 185], "2": [9, 0, 139], "3": [12, 0, 120] },
      { "1": [34, 0, 185], "2": [26, 0, 139], "3": [20, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [5, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[10, 0, 43]]
      }
    ]
  },
  "1005770": {
    "sekolah": "SMK NEGERI 3",
    "kompetensi": [
      "Teknik Komputer dan Jaringan",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1872, 1873, 1874, 1875],
    "kapasitas": [[[11, 0, 46]], [[11, 0, 46]], [[13, 0, 46]], [[11, 0, 46]]],
    "rekap": [
      ["47.06", "49.35", "48.04"],
      ["48.91", "50.39", "49.51"],
      ["47.79", "53.23", "49.58"],
      ["47.81", "50.08", "48.57"]
    ],
    "peminat": [
      { "1": [49, 0, 185], "2": [34, 0, 139], "3": [45, 0, 120] },
      { "1": [53, 0, 185], "2": [46, 0, 139], "3": [39, 0, 120] },
      { "1": [24, 0, 185], "2": [25, 0, 139], "3": [19, 0, 120] },
      { "1": [33, 0, 185], "2": [33, 0, 139], "3": [30, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005771": {
    "sekolah": "SMK NEGERI 4",
    "kompetensi": [
      "Teknik Konstruksi dan Perumahan",
      "Desain dan Teknik Furnitur",
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pemesinan",
      "Teknik Pengelasan",
      "Teknik Kendaraan Ringan",
      "Teknik Audio Video",
      "Teknik Elektronika Industri",
      "Teknik Mekatronika",
      "Teknik Komputer dan Jaringan"
    ],
    "k_kompetensi": [
      1877, 1876, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885
    ],
    "kapasitas": [
      [[24, 0, 46]],
      [[13, 0, 46]],
      [[27, 0, 46]],
      [[27, 0, 46]],
      [[13, 0, 46]],
      [[23, 0, 46]],
      [[12, 0, 46]],
      [[24, 0, 46]],
      [[11, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["47.04", "50.44", "48.60"],
      ["48.08", "50.23", "49.07"],
      ["46.78", "50.00", "47.83"],
      ["46.81", "53.45", "48.20"],
      ["47.44", "49.96", "48.41"],
      ["47.45", "50.12", "48.73"],
      ["47.13", "53.20", "49.12"],
      ["46.99", "50.97", "48.54"],
      ["46.88", "49.71", "48.18"],
      ["50.30", "53.51", "51.65"]
    ],
    "peminat": [
      { "1": [58, 0, 185], "2": [71, 0, 139], "3": [44, 0, 120] },
      { "1": [45, 0, 185], "2": [43, 0, 139], "3": [28, 0, 120] },
      { "1": [88, 0, 185], "2": [61, 0, 139], "3": [59, 0, 120] },
      { "1": [101, 0, 185], "2": [68, 0, 139], "3": [48, 0, 120] },
      { "1": [61, 0, 185], "2": [52, 0, 139], "3": [44, 0, 120] },
      { "1": [135, 0, 185], "2": [65, 0, 139], "3": [56, 0, 120] },
      { "1": [31, 0, 185], "2": [25, 0, 139], "3": [33, 0, 120] },
      { "1": [46, 0, 185], "2": [37, 0, 139], "3": [44, 0, 120] },
      { "1": [29, 0, 185], "2": [25, 0, 139], "3": [33, 0, 120] },
      { "1": [59, 0, 185], "2": [39, 0, 139], "3": [42, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [6, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [5, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005772": {
    "sekolah": "SMK NEGERI 5",
    "kompetensi": [
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pemanasan, Tata Udara, dan Pendinginan",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Teknik Sepeda Motor",
      "Teknik Audio Video"
    ],
    "k_kompetensi": [1886, 1889, 1887, 1888, 1891, 1890],
    "kapasitas": [
      [[25, 0, 46]],
      [[12, 0, 46]],
      [[26, 0, 46]],
      [[23, 0, 46]],
      [[11, 0, 46]],
      [[27, 0, 46]]
    ],
    "rekap": [
      ["47.31", "51.02", "48.26"],
      ["46.05", "48.80", "46.90"],
      ["46.42", "53.00", "47.76"],
      ["47.10", "49.25", "47.99"],
      ["46.29", "47.40", "46.82"],
      ["46.27", "49.42", "47.25"]
    ],
    "peminat": [
      { "1": [83, 0, 185], "2": [57, 0, 139], "3": [36, 0, 120] },
      { "1": [33, 0, 185], "2": [36, 0, 139], "3": [23, 0, 120] },
      { "1": [73, 0, 185], "2": [55, 0, 139], "3": [47, 0, 120] },
      { "1": [113, 0, 185], "2": [94, 0, 139], "3": [53, 0, 120] },
      { "1": [50, 0, 185], "2": [42, 0, 139], "3": [29, 0, 120] },
      { "1": [66, 0, 185], "2": [49, 0, 139], "3": [42, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [7, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [7, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [12, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [5, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      }
    ]
  },
  "1005773": {
    "sekolah": "SMK NEGERI 6",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Animasi",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1892, 1894, 1893, 1895, 1896, 1897],
    "kapasitas": [
      [[12, 0, 46]],
      [[12, 0, 46]],
      [[25, 0, 46]],
      [[11, 0, 46]],
      [[27, 0, 46]],
      [[25, 0, 46]]
    ],
    "rekap": [
      ["46.79", "56.85", "48.57"],
      ["45.42", "49.31", "46.24"],
      ["45.99", "50.07", "47.38"],
      ["48.82", "52.63", "49.93"],
      ["46.79", "55.81", "49.00"],
      ["47.36", "51.87", "48.58"]
    ],
    "peminat": [
      { "1": [34, 0, 185], "2": [23, 0, 139], "3": [13, 0, 120] },
      { "1": [35, 0, 185], "2": [17, 0, 139], "3": [5, 0, 120] },
      { "1": [53, 0, 185], "2": [26, 0, 139], "3": [19, 0, 120] },
      { "1": [71, 0, 185], "2": [34, 0, 139], "3": [31, 0, 120] },
      { "1": [48, 0, 185], "2": [17, 0, 139], "3": [17, 0, 120] },
      { "1": [63, 0, 185], "2": [26, 0, 139], "3": [43, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [26, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005774": {
    "sekolah": "SMK NEGERI 7",
    "kompetensi": [
      "Teknik Grafika",
      "Teknik Komputer dan Jaringan",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [1898, 1899, 1900],
    "kapasitas": [[[36, 0, 46]], [[23, 0, 46]], [[35, 0, 46]]],
    "rekap": [
      ["46.14", "50.32", "47.06"],
      ["47.70", "52.23", "49.14"],
      ["46.65", "50.94", "47.80"]
    ],
    "peminat": [
      { "1": [86, 0, 185], "2": [70, 0, 139], "3": [41, 0, 120] },
      { "1": [56, 0, 185], "2": [70, 0, 139], "3": [55, 0, 120] },
      { "1": [63, 0, 185], "2": [60, 0, 139], "3": [41, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [11, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[36, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [7, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [24, 0, 43], "2": [7, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[35, 0, 43]]
      }
    ]
  },
  "1005775": {
    "sekolah": "SMK NEGERI 8",
    "kompetensi": [
      "Manajemen Logistik",
      "Rekayasa Perangkat Lunak",
      "Usaha Layanan Wisata",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1907, 1906, 1901, 1902, 1903, 1905, 1904],
    "kapasitas": [
      [[12, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[40, 0, 46]],
      [[13, 0, 46]],
      [[25, 0, 46]]
    ],
    "rekap": [
      ["47.02", "52.74", "48.42"],
      ["48.55", "53.71", "50.46"],
      ["47.08", "50.25", "48.54"],
      ["50.18", "53.94", "51.40"],
      ["47.62", "56.06", "49.92"],
      ["47.31", "51.52", "48.51"],
      ["46.54", "50.34", "48.04"]
    ],
    "peminat": [
      { "1": [28, 0, 185], "2": [11, 0, 139], "3": [4, 0, 120] },
      { "1": [29, 0, 185], "2": [17, 0, 139], "3": [17, 0, 120] },
      { "1": [26, 0, 185], "2": [27, 0, 139], "3": [23, 0, 120] },
      { "1": [64, 0, 185], "2": [35, 0, 139], "3": [33, 0, 120] },
      { "1": [66, 0, 185], "2": [25, 0, 139], "3": [10, 0, 120] },
      { "1": [30, 0, 185], "2": [24, 0, 139], "3": [17, 0, 120] },
      { "1": [45, 0, 185], "2": [34, 0, 139], "3": [26, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [40, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[40, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005776": {
    "sekolah": "SMK NEGERI 9",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Usaha Layanan Wisata",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1908, 1909, 1910, 1911, 1913, 1912],
    "kapasitas": [
      [[13, 0, 46]],
      [[12, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["48.17", "51.60", "49.48"],
      ["48.44", "51.89", "49.97"],
      ["50.40", "52.83", "51.04"],
      ["49.22", "52.19", "50.22"],
      ["48.90", "52.60", "50.31"],
      ["48.45", "51.60", "49.62"]
    ],
    "peminat": [
      { "1": [40, 0, 185], "2": [25, 0, 139], "3": [11, 0, 120] },
      { "1": [36, 0, 185], "2": [18, 0, 139], "3": [20, 0, 120] },
      { "1": [96, 0, 185], "2": [62, 0, 139], "3": [55, 0, 120] },
      { "1": [29, 0, 185], "2": [25, 0, 139], "3": [17, 0, 120] },
      { "1": [30, 0, 185], "2": [27, 0, 139], "3": [22, 0, 120] },
      { "1": [53, 0, 185], "2": [41, 0, 139], "3": [36, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005777": {
    "sekolah": "SMK NEGERI 10",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Manajemen Logistik",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1914, 1916, 1915, 1917, 1919, 1918],
    "kapasitas": [
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[26, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["48.25", "51.90", "50.07"],
      ["47.48", "51.15", "48.33"],
      ["49.46", "51.27", "50.27"],
      ["47.14", "52.12", "49.12"],
      ["46.96", "50.28", "47.63"],
      ["47.64", "52.40", "48.85"]
    ],
    "peminat": [
      { "1": [32, 0, 185], "2": [22, 0, 139], "3": [20, 0, 120] },
      { "1": [36, 0, 185], "2": [16, 0, 139], "3": [13, 0, 120] },
      { "1": [69, 0, 185], "2": [49, 0, 139], "3": [28, 0, 120] },
      { "1": [43, 0, 185], "2": [23, 0, 139], "3": [21, 0, 120] },
      { "1": [20, 0, 185], "2": [24, 0, 139], "3": [21, 0, 120] },
      { "1": [19, 0, 185], "2": [29, 0, 139], "3": [18, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005778": {
    "sekolah": "SMK NEGERI 11",
    "kompetensi": ["Manajemen Perkantoran", "Akuntansi", "Bisnis Retail"],
    "k_kompetensi": [1920, 1921, 1922],
    "kapasitas": [[[23, 0, 46]], [[25, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["48.48", "51.97", "49.50"],
      ["47.68", "56.57", "49.17"],
      ["47.68", "57.73", "49.02"]
    ],
    "peminat": [
      { "1": [76, 0, 185], "2": [95, 0, 139], "3": [90, 0, 120] },
      { "1": [43, 0, 185], "2": [39, 0, 139], "3": [35, 0, 120] },
      { "1": [57, 0, 185], "2": [84, 0, 139], "3": [72, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [7, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [9, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005779": {
    "sekolah": "SMK NEGERI 12",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1923, 1924, 1925, 1926],
    "kapasitas": [[[23, 0, 46]], [[10, 0, 46]], [[24, 0, 46]], [[21, 0, 46]]],
    "rekap": [
      ["48.47", "53.22", "50.35"],
      ["52.09", "54.08", "53.19"],
      ["49.08", "53.23", "50.50"],
      ["49.40", "52.12", "50.74"]
    ],
    "peminat": [
      { "1": [78, 0, 185], "2": [24, 0, 139], "3": [25, 0, 120] },
      { "1": [124, 0, 185], "2": [54, 0, 139], "3": [34, 0, 120] },
      { "1": [46, 0, 185], "2": [41, 0, 139], "3": [15, 0, 120] },
      { "1": [55, 0, 185], "2": [31, 0, 139], "3": [30, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[10, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[21, 0, 43]]
      }
    ]
  },
  "1005780": {
    "sekolah": "SMK NEGERI 13",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Usaha Layanan Wisata",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1931, 1927, 1928, 1929, 1930],
    "kapasitas": [
      [[11, 0, 46]],
      [[23, 0, 46]],
      [[23, 0, 46]],
      [[38, 0, 46]],
      [[23, 0, 46]]
    ],
    "rekap": [
      ["48.54", "53.21", "50.03"],
      ["48.31", "54.74", "49.47"],
      ["50.61", "54.93", "51.62"],
      ["49.05", "54.70", "50.50"],
      ["49.00", "51.86", "49.96"]
    ],
    "peminat": [
      { "1": [51, 0, 185], "2": [40, 0, 139], "3": [31, 0, 120] },
      { "1": [71, 0, 185], "2": [40, 0, 139], "3": [51, 0, 120] },
      { "1": [138, 0, 185], "2": [114, 0, 139], "3": [61, 0, 120] },
      { "1": [79, 0, 185], "2": [41, 0, 139], "3": [35, 0, 120] },
      { "1": [144, 0, 185], "2": [102, 0, 139], "3": [59, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [31, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005781": {
    "sekolah": "SMK NEGERI 14",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1932, 1933, 1934, 1935],
    "kapasitas": [[[25, 0, 46]], [[24, 0, 46]], [[40, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["46.43", "51.35", "47.97"],
      ["47.66", "52.15", "48.97"],
      ["46.40", "58.24", "48.47"],
      ["47.58", "51.86", "48.68"]
    ],
    "peminat": [
      { "1": [39, 0, 185], "2": [49, 0, 139], "3": [37, 0, 120] },
      { "1": [75, 0, 185], "2": [53, 0, 139], "3": [47, 0, 120] },
      { "1": [55, 0, 185], "2": [44, 0, 139], "3": [40, 0, 120] },
      { "1": [49, 0, 185], "2": [58, 0, 139], "3": [30, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [8, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [32, 0, 43], "2": [5, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[40, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005782": {
    "sekolah": "SMK NEGERI 15",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1936, 1937, 1938, 1939],
    "kapasitas": [[[12, 0, 46]], [[27, 0, 46]], [[27, 0, 46]], [[27, 0, 46]]],
    "rekap": [
      ["46.04", "50.08", "47.19"],
      ["46.97", "50.58", "48.28"],
      ["46.32", "50.24", "47.31"],
      ["46.60", "49.53", "47.63"]
    ],
    "peminat": [
      { "1": [20, 0, 185], "2": [29, 0, 139], "3": [29, 0, 120] },
      { "1": [45, 0, 185], "2": [65, 0, 139], "3": [49, 0, 120] },
      { "1": [40, 0, 185], "2": [35, 0, 139], "3": [29, 0, 120] },
      { "1": [50, 0, 185], "2": [76, 0, 139], "3": [58, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [3, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [9, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [8, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      }
    ]
  },
  "1005783": {
    "sekolah": "SMK NEGERI 16",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1940, 1941, 1942, 1943],
    "kapasitas": [[[11, 0, 46]], [[22, 0, 46]], [[26, 0, 46]], [[11, 0, 46]]],
    "rekap": [
      ["48.14", "49.97", "48.97"],
      ["48.40", "52.77", "49.87"],
      ["46.45", "51.03", "48.07"],
      ["46.98", "50.71", "47.80"]
    ],
    "peminat": [
      { "1": [32, 0, 185], "2": [16, 0, 139], "3": [17, 0, 120] },
      { "1": [65, 0, 185], "2": [58, 0, 139], "3": [41, 0, 120] },
      { "1": [42, 0, 185], "2": [29, 0, 139], "3": [21, 0, 120] },
      { "1": [31, 0, 185], "2": [29, 0, 139], "3": [30, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005784": {
    "sekolah": "SMK NEGERI 17",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1944, 1945, 1946, 1947],
    "kapasitas": [[[11, 0, 46]], [[11, 0, 46]], [[23, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["48.45", "52.32", "49.64"],
      ["49.26", "52.06", "50.14"],
      ["47.95", "51.81", "49.07"],
      ["48.16", "50.11", "48.75"]
    ],
    "peminat": [
      { "1": [42, 0, 185], "2": [48, 0, 139], "3": [27, 0, 120] },
      { "1": [70, 0, 185], "2": [96, 0, 139], "3": [95, 0, 120] },
      { "1": [37, 0, 185], "2": [67, 0, 139], "3": [59, 0, 120] },
      { "1": [60, 0, 185], "2": [108, 0, 139], "3": [81, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005785": {
    "sekolah": "SMK NEGERI 18",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1948, 1949, 1950, 1951],
    "kapasitas": [[[13, 0, 46]], [[13, 0, 46]], [[40, 0, 46]], [[12, 0, 46]]],
    "rekap": [
      ["45.81", "49.10", "47.02"],
      ["47.79", "50.62", "48.59"],
      ["45.75", "51.03", "47.30"],
      ["46.97", "50.75", "48.58"]
    ],
    "peminat": [
      { "1": [24, 0, 185], "2": [28, 0, 139], "3": [24, 0, 120] },
      { "1": [46, 0, 185], "2": [26, 0, 139], "3": [26, 0, 120] },
      { "1": [68, 0, 185], "2": [36, 0, 139], "3": [32, 0, 120] },
      { "1": [36, 0, 185], "2": [23, 0, 139], "3": [28, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [24, 0, 43], "2": [12, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[40, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005786": {
    "sekolah": "SMK NEGERI 19",
    "kompetensi": [
      "Produksi Film",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1952, 1953, 1954, 1955],
    "kapasitas": [[[22, 0, 46]], [[11, 0, 46]], [[25, 0, 46]], [[11, 0, 46]]],
    "rekap": [
      ["46.79", "50.68", "48.14"],
      ["48.83", "51.82", "49.71"],
      ["47.02", "51.11", "48.40"],
      ["47.88", "50.71", "48.87"]
    ],
    "peminat": [
      { "1": [39, 0, 185], "2": [27, 0, 139], "3": [29, 0, 120] },
      { "1": [44, 0, 185], "2": [44, 0, 139], "3": [32, 0, 120] },
      { "1": [36, 0, 185], "2": [31, 0, 139], "3": [20, 0, 120] },
      { "1": [28, 0, 185], "2": [28, 0, 139], "3": [45, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [2, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005787": {
    "sekolah": "SMK NEGERI 20",
    "kompetensi": [
      "Manajemen Logistik",
      "Rekayasa Perangkat Lunak",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Layanan Perbankan Syariah",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1962, 1961, 1956, 1957, 1959, 1960, 1958],
    "kapasitas": [
      [[13, 0, 46]],
      [[12, 0, 46]],
      [[12, 0, 46]],
      [[27, 0, 46]],
      [[12, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["45.84", "49.10", "46.73"],
      ["46.01", "49.57", "47.05"],
      ["47.88", "54.81", "49.53"],
      ["45.87", "52.84", "47.51"],
      ["45.99", "50.01", "47.17"],
      ["45.50", "50.66", "46.66"],
      ["46.72", "49.68", "47.97"]
    ],
    "peminat": [
      { "1": [23, 0, 185], "2": [29, 0, 139], "3": [21, 0, 120] },
      { "1": [22, 0, 185], "2": [7, 0, 139], "3": [13, 0, 120] },
      { "1": [44, 0, 185], "2": [59, 0, 139], "3": [37, 0, 120] },
      { "1": [42, 0, 185], "2": [29, 0, 139], "3": [28, 0, 120] },
      { "1": [15, 0, 185], "2": [36, 0, 139], "3": [17, 0, 120] },
      { "1": [25, 0, 185], "2": [31, 0, 139], "3": [25, 0, 120] },
      { "1": [36, 0, 185], "2": [41, 0, 139], "3": [24, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005788": {
    "sekolah": "SMK NEGERI 21",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1963, 1964, 1965, 1966],
    "kapasitas": [[[13, 0, 46]], [[11, 0, 46]], [[27, 0, 46]], [[12, 0, 46]]],
    "rekap": [
      ["45.94", "48.23", "46.64"],
      ["47.95", "49.93", "48.76"],
      ["46.23", "49.94", "47.28"],
      ["46.69", "48.73", "47.38"]
    ],
    "peminat": [
      { "1": [29, 0, 185], "2": [27, 0, 139], "3": [27, 0, 120] },
      { "1": [27, 0, 185], "2": [50, 0, 139], "3": [34, 0, 120] },
      { "1": [37, 0, 185], "2": [37, 0, 139], "3": [35, 0, 120] },
      { "1": [23, 0, 185], "2": [33, 0, 139], "3": [43, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [2, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [5, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [1, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005789": {
    "sekolah": "SMK NEGERI 22",
    "kompetensi": [
      "Teknik Komputer dan Jaringan",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital"
    ],
    "k_kompetensi": [1967, 1968, 1969, 1970],
    "kapasitas": [[[23, 0, 46]], [[11, 0, 46]], [[23, 0, 46]], [[11, 0, 46]]],
    "rekap": [
      ["47.72", "52.52", "49.22"],
      ["49.25", "51.51", "50.29"],
      ["47.03", "52.25", "48.72"],
      ["47.67", "51.75", "49.34"]
    ],
    "peminat": [
      { "1": [81, 0, 185], "2": [48, 0, 139], "3": [33, 0, 120] },
      { "1": [91, 0, 185], "2": [68, 0, 139], "3": [41, 0, 120] },
      { "1": [44, 0, 185], "2": [38, 0, 139], "3": [28, 0, 120] },
      { "1": [47, 0, 185], "2": [36, 0, 139], "3": [37, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005790": {
    "sekolah": "SMK NEGERI 23",
    "kompetensi": [
      "Desain dan Produksi Busana",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [1971, 1972, 1973, 1975, 1974],
    "kapasitas": [
      [[13, 0, 46]],
      [[24, 0, 46]],
      [[27, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]]
    ],
    "rekap": [
      ["46.79", "50.07", "47.62"],
      ["48.17", "51.87", "49.36"],
      ["47.00", "51.46", "48.24"],
      ["47.17", "50.20", "47.97"],
      ["47.60", "49.76", "48.33"]
    ],
    "peminat": [
      { "1": [20, 0, 185], "2": [21, 0, 139], "3": [19, 0, 120] },
      { "1": [77, 0, 185], "2": [77, 0, 139], "3": [47, 0, 120] },
      { "1": [33, 0, 185], "2": [47, 0, 139], "3": [14, 0, 120] },
      { "1": [22, 0, 185], "2": [25, 0, 139], "3": [42, 0, 120] },
      { "1": [24, 0, 185], "2": [48, 0, 139], "3": [39, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [8, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  },
  "1005791": {
    "sekolah": "SMK NEGERI 24",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Usaha Layanan Wisata",
      "Perhotelan",
      "Kuliner",
      "Desain dan Produksi Busana"
    ],
    "k_kompetensi": [1976, 1977, 1978, 1979, 1980],
    "kapasitas": [
      [[23, 0, 46]],
      [[11, 0, 46]],
      [[34, 0, 46]],
      [[33, 0, 46]],
      [[38, 0, 46]]
    ],
    "rekap": [
      ["47.94", "53.31", "50.22"],
      ["46.48", "51.86", "48.25"],
      ["47.23", "53.83", "48.54"],
      ["46.64", "51.11", "48.00"],
      ["45.17", "49.20", "46.38"]
    ],
    "peminat": [
      { "1": [47, 0, 185], "2": [35, 0, 139], "3": [24, 0, 120] },
      { "1": [23, 0, 185], "2": [14, 0, 139], "3": [21, 0, 120] },
      { "1": [88, 0, 185], "2": [68, 0, 139], "3": [63, 0, 120] },
      { "1": [72, 0, 185], "2": [59, 0, 139], "3": [52, 0, 120] },
      { "1": [69, 0, 185], "2": [25, 0, 139], "3": [30, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [30, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[34, 0, 43]]
      },
      {
        "by-pilihan": { "1": [28, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[33, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [7, 0, 13], "3": [8, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      }
    ]
  },
  "1005792": {
    "sekolah": "SMK NEGERI 25",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital"
    ],
    "k_kompetensi": [1984, 1981, 1982, 1983],
    "kapasitas": [[[12, 0, 46]], [[12, 0, 46]], [[27, 0, 46]], [[13, 0, 46]]],
    "rekap": [
      ["46.61", "50.34", "48.38"],
      ["47.93", "52.94", "49.14"],
      ["46.41", "53.72", "47.88"],
      ["46.55", "49.08", "47.34"]
    ],
    "peminat": [
      { "1": [27, 0, 185], "2": [47, 0, 139], "3": [37, 0, 120] },
      { "1": [62, 0, 185], "2": [86, 0, 139], "3": [72, 0, 120] },
      { "1": [54, 0, 185], "2": [71, 0, 139], "3": [43, 0, 120] },
      { "1": [37, 0, 185], "2": [58, 0, 139], "3": [49, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [5, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [7, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  },
  "1005793": {
    "sekolah": "SMK NEGERI 26",
    "kompetensi": [
      "Konstruksi Gedung dan Sanitasi",
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Fabrikasi Logam dan Manufaktur",
      "Teknik Kendaraan Ringan",
      "Teknik Bodi Kendaraan Ringan",
      "Sistem Informasi, Jaringan dan Aplikasi",
      "Teknik Elektronika Komunikasi"
    ],
    "k_kompetensi": [1985, 1986, 1987, 1988, 1991, 1989, 1990],
    "kapasitas": [
      [[25, 0, 46]],
      [[23, 0, 46]],
      [[26, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[23, 0, 46]],
      [[23, 0, 46]]
    ],
    "rekap": [
      ["48.35", "55.78", "50.40"],
      ["49.24", "53.21", "50.34"],
      ["47.97", "52.92", "49.71"],
      ["50.40", "55.01", "52.03"],
      ["47.27", "50.40", "48.36"],
      ["52.85", "64.53", "55.30"],
      ["48.42", "55.58", "50.52"]
    ],
    "peminat": [
      { "1": [36, 0, 185], "2": [12, 0, 139], "3": [5, 0, 120] },
      { "1": [70, 0, 185], "2": [37, 0, 139], "3": [29, 0, 120] },
      { "1": [44, 0, 185], "2": [14, 0, 139], "3": [17, 0, 120] },
      { "1": [93, 0, 185], "2": [81, 0, 139], "3": [55, 0, 120] },
      { "1": [14, 0, 185], "2": [18, 0, 139], "3": [16, 0, 120] },
      { "1": [88, 0, 185], "2": [20, 0, 139], "3": [37, 0, 120] },
      { "1": [27, 0, 185], "2": [17, 0, 139], "3": [19, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [25, 0, 43], "2": [0, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [5, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005794": {
    "sekolah": "SMK NEGERI 27",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Usaha Layanan Wisata",
      "Perhotelan",
      "Kuliner",
      "Tata Kecantikan Kulit dan Rambut",
      "Desain dan Produksi Busana"
    ],
    "k_kompetensi": [1997, 1992, 1993, 1994, 1995, 1996],
    "kapasitas": [
      [[13, 0, 46]],
      [[26, 0, 46]],
      [[33, 0, 46]],
      [[34, 0, 46]],
      [[11, 0, 46]],
      [[26, 0, 46]]
    ],
    "rekap": [
      ["47.62", "49.52", "48.33"],
      ["48.19", "51.91", "49.17"],
      ["49.22", "53.60", "50.54"],
      ["48.55", "56.41", "49.92"],
      ["49.26", "52.67", "50.35"],
      ["46.74", "49.69", "47.97"]
    ],
    "peminat": [
      { "1": [34, 0, 185], "2": [28, 0, 139], "3": [33, 0, 120] },
      { "1": [42, 0, 185], "2": [35, 0, 139], "3": [32, 0, 120] },
      { "1": [84, 0, 185], "2": [66, 0, 139], "3": [55, 0, 120] },
      { "1": [86, 0, 185], "2": [53, 0, 139], "3": [56, 0, 120] },
      { "1": [40, 0, 185], "2": [21, 0, 139], "3": [43, 0, 120] },
      { "1": [48, 0, 185], "2": [28, 0, 139], "3": [38, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [32, 0, 43], "2": [0, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[33, 0, 43]]
      },
      {
        "by-pilihan": { "1": [30, 0, 43], "2": [1, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[34, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      }
    ]
  },
  "1005795": {
    "sekolah": "SMK NEGERI 28",
    "kompetensi": [
      "Layanan Penunjang Keperawatan dan Caregiving",
      "Pekerjaan Sosial",
      "Perhotelan",
      "Kuliner"
    ],
    "k_kompetensi": [1998, 1999, 2000, 2001],
    "kapasitas": [[[13, 0, 46]], [[39, 0, 46]], [[38, 0, 46]], [[22, 0, 46]]],
    "rekap": [
      ["49.37", "54.01", "51.66"],
      ["45.50", "49.00", "46.79"],
      ["46.93", "50.68", "48.39"],
      ["47.92", "50.05", "48.83"]
    ],
    "peminat": [
      { "1": [37, 0, 185], "2": [12, 0, 139], "3": [14, 0, 120] },
      { "1": [59, 0, 185], "2": [57, 0, 139], "3": [43, 0, 120] },
      { "1": [73, 0, 185], "2": [73, 0, 139], "3": [70, 0, 120] },
      { "1": [52, 0, 185], "2": [52, 0, 139], "3": [49, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [28, 0, 43], "2": [9, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[39, 0, 43]]
      },
      {
        "by-pilihan": { "1": [25, 0, 43], "2": [6, 0, 13], "3": [7, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      }
    ]
  },
  "1005796": {
    "sekolah": "SMK NEGERI 29",
    "kompetensi": [
      "Teknik Pemanasan, Tata Udara, dan Pendinginan",
      "Airframe Powerplant",
      "Electrical Avionic",
      "Teknik Elektronika Industri"
    ],
    "k_kompetensi": [2002, 2003, 2004, 2005],
    "kapasitas": [[[24, 0, 46]], [[38, 0, 46]], [[26, 0, 46]], [[39, 0, 46]]],
    "rekap": [
      ["45.32", "53.12", "46.72"],
      ["45.23", "51.76", "47.21"],
      ["45.10", "47.26", "45.98"],
      ["45.07", "48.87", "46.26"]
    ],
    "peminat": [
      { "1": [50, 0, 185], "2": [33, 0, 139], "3": [23, 0, 120] },
      { "1": [62, 0, 185], "2": [41, 0, 139], "3": [22, 0, 120] },
      { "1": [51, 0, 185], "2": [63, 0, 139], "3": [32, 0, 120] },
      { "1": [58, 0, 185], "2": [44, 0, 139], "3": [53, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [32, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [6, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [28, 0, 43], "2": [7, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[39, 0, 43]]
      }
    ]
  },
  "1005797": {
    "sekolah": "SMK NEGERI 30",
    "kompetensi": ["Perhotelan", "Kuliner", "Desain dan Produksi Busana"],
    "k_kompetensi": [2006, 2007, 2008],
    "kapasitas": [[[11, 0, 46]], [[34, 0, 46]], [[24, 0, 46]]],
    "rekap": [
      ["48.76", "51.22", "49.83"],
      ["47.92", "51.58", "49.06"],
      ["45.94", "48.95", "46.74"]
    ],
    "peminat": [
      { "1": [67, 0, 185], "2": [53, 0, 139], "3": [41, 0, 120] },
      { "1": [80, 0, 185], "2": [49, 0, 139], "3": [40, 0, 120] },
      { "1": [36, 0, 185], "2": [36, 0, 139], "3": [32, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [32, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[34, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [6, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      }
    ]
  },
  "1005798": {
    "sekolah": "SMK NEGERI 31",
    "kompetensi": [
      "Animasi",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Layanan Perbankan",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2009, 2010, 2011, 2012, 2013, 2014],
    "kapasitas": [
      [[12, 0, 46]],
      [[13, 0, 46]],
      [[10, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["45.74", "47.59", "46.01"],
      ["46.04", "49.85", "46.78"],
      ["47.81", "49.59", "48.75"],
      ["46.35", "49.71", "47.39"],
      ["46.01", "51.43", "47.18"],
      ["46.88", "49.18", "47.64"]
    ],
    "peminat": [
      { "1": [44, 0, 185], "2": [19, 0, 139], "3": [19, 0, 120] },
      { "1": [24, 0, 185], "2": [28, 0, 139], "3": [37, 0, 120] },
      { "1": [20, 0, 185], "2": [47, 0, 139], "3": [36, 0, 120] },
      { "1": [15, 0, 185], "2": [35, 0, 139], "3": [19, 0, 120] },
      { "1": [23, 0, 185], "2": [24, 0, 139], "3": [15, 0, 120] },
      { "1": [42, 0, 185], "2": [45, 0, 139], "3": [36, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [0, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[10, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005799": {
    "sekolah": "SMK NEGERI 32",
    "kompetensi": ["Perhotelan", "Kuliner", "Desain dan Produksi Busana"],
    "k_kompetensi": [2015, 2016, 2017],
    "kapasitas": [[[23, 0, 46]], [[33, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["47.82", "51.69", "49.14"],
      ["47.51", "53.82", "49.08"],
      ["46.02", "49.18", "47.19"]
    ],
    "peminat": [
      { "1": [96, 0, 185], "2": [52, 0, 139], "3": [52, 0, 120] },
      { "1": [73, 0, 185], "2": [62, 0, 139], "3": [47, 0, 120] },
      { "1": [34, 0, 185], "2": [20, 0, 139], "3": [22, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [30, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[33, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005800": {
    "sekolah": "SMK NEGERI 33",
    "kompetensi": [
      "Usaha Layanan Wisata",
      "Perhotelan",
      "Kuliner",
      "Desain dan Produksi Busana"
    ],
    "k_kompetensi": [2018, 2019, 2020, 2021],
    "kapasitas": [[[13, 0, 46]], [[21, 0, 46]], [[23, 0, 46]], [[13, 0, 46]]],
    "rekap": [
      ["48.28", "53.42", "50.34"],
      ["48.32", "51.90", "49.52"],
      ["47.38", "52.88", "48.95"],
      ["47.29", "52.04", "48.65"]
    ],
    "peminat": [
      { "1": [27, 0, 185], "2": [21, 0, 139], "3": [23, 0, 120] },
      { "1": [61, 0, 185], "2": [63, 0, 139], "3": [43, 0, 120] },
      { "1": [59, 0, 185], "2": [37, 0, 139], "3": [32, 0, 120] },
      { "1": [20, 0, 185], "2": [24, 0, 139], "3": [16, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[21, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [5, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  },
  "1005801": {
    "sekolah": "SMK NEGERI 34",
    "kompetensi": [
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Teknik Sepeda Motor",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [2022, 2023, 2024, 2025, 2026],
    "kapasitas": [
      [[25, 0, 46]],
      [[13, 0, 46]],
      [[25, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["45.68", "48.92", "46.55"],
      ["45.56", "48.58", "46.37"],
      ["45.73", "52.73", "46.77"],
      ["45.64", "47.95", "46.73"],
      ["46.50", "48.91", "47.50"]
    ],
    "peminat": [
      { "1": [37, 0, 185], "2": [54, 0, 139], "3": [50, 0, 120] },
      { "1": [30, 0, 185], "2": [40, 0, 139], "3": [39, 0, 120] },
      { "1": [49, 0, 185], "2": [78, 0, 139], "3": [65, 0, 120] },
      { "1": [37, 0, 185], "2": [36, 0, 139], "3": [33, 0, 120] },
      { "1": [20, 0, 185], "2": [36, 0, 139], "3": [28, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [9, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [4, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [8, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [5, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005802": {
    "sekolah": "SMK NEGERI 35",
    "kompetensi": [
      "Desain Pemodelan dan Informasi Bangunan",
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Teknik Audio Video"
    ],
    "k_kompetensi": [2027, 2028, 2029, 2030, 2031],
    "kapasitas": [
      [[27, 0, 46]],
      [[26, 0, 46]],
      [[23, 0, 46]],
      [[26, 0, 46]],
      [[24, 0, 46]]
    ],
    "rekap": [
      ["46.26", "50.01", "47.55"],
      ["46.29", "49.10", "47.33"],
      ["46.09", "48.59", "47.03"],
      ["46.42", "48.82", "47.44"],
      ["46.32", "49.41", "47.20"]
    ],
    "peminat": [
      { "1": [52, 0, 185], "2": [53, 0, 139], "3": [43, 0, 120] },
      { "1": [64, 0, 185], "2": [76, 0, 139], "3": [56, 0, 120] },
      { "1": [73, 0, 185], "2": [77, 0, 139], "3": [58, 0, 120] },
      { "1": [96, 0, 185], "2": [103, 0, 139], "3": [81, 0, 120] },
      { "1": [60, 0, 185], "2": [41, 0, 139], "3": [65, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [7, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [8, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [6, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      }
    ]
  },
  "1005803": {
    "sekolah": "SMK NEGERI 36",
    "kompetensi": [
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Teknik Alat Berat",
      "Nautika Kapal Penangkapan Ikan",
      "Teknika Kapal Penangkapan Ikan",
      "Teknik Komputer dan Jaringan",
      "Desain Komunikasi Visual",
      "Agribisnis Ikan Hias"
    ],
    "k_kompetensi": [2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039],
    "kapasitas": [
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]],
      [[11, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["46.62", "51.44", "48.28"],
      ["47.40", "53.40", "48.75"],
      ["46.68", "50.36", "47.73"],
      ["46.36", "49.75", "47.41"],
      ["46.25", "49.42", "47.11"],
      ["48.39", "52.84", "49.83"],
      ["48.47", "52.38", "50.12"],
      ["47.10", "49.68", "47.96"]
    ],
    "peminat": [
      { "1": [46, 0, 185], "2": [40, 0, 139], "3": [25, 0, 120] },
      { "1": [55, 0, 185], "2": [60, 0, 139], "3": [33, 0, 120] },
      { "1": [29, 0, 185], "2": [21, 0, 139], "3": [38, 0, 120] },
      { "1": [34, 0, 185], "2": [30, 0, 139], "3": [24, 0, 120] },
      { "1": [31, 0, 185], "2": [40, 0, 139], "3": [22, 0, 120] },
      { "1": [33, 0, 185], "2": [33, 0, 139], "3": [38, 0, 120] },
      { "1": [25, 0, 185], "2": [27, 0, 139], "3": [19, 0, 120] },
      { "1": [29, 0, 185], "2": [21, 0, 139], "3": [28, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [1, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [0, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [1, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005804": {
    "sekolah": "SMK NEGERI 37",
    "kompetensi": ["Perhotelan", "Kuliner", "Desain dan Produksi Busana"],
    "k_kompetensi": [2040, 2041, 2042],
    "kapasitas": [[[23, 0, 46]], [[34, 0, 46]], [[27, 0, 46]]],
    "rekap": [
      ["47.13", "52.00", "48.26"],
      ["46.95", "50.71", "47.97"],
      ["45.47", "47.68", "46.11"]
    ],
    "peminat": [
      { "1": [65, 0, 185], "2": [104, 0, 139], "3": [97, 0, 120] },
      { "1": [81, 0, 185], "2": [97, 0, 139], "3": [71, 0, 120] },
      { "1": [32, 0, 185], "2": [38, 0, 139], "3": [39, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [7, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [10, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[34, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [6, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      }
    ]
  },
  "1005805": {
    "sekolah": "SMK NEGERI 38",
    "kompetensi": ["Perhotelan", "Kuliner", "Desain dan Produksi Busana"],
    "k_kompetensi": [2043, 2044, 2045],
    "kapasitas": [[[23, 0, 46]], [[23, 0, 46]], [[27, 0, 46]]],
    "rekap": [
      ["46.82", "50.84", "47.88"],
      ["47.64", "50.98", "48.89"],
      ["45.93", "48.80", "46.98"]
    ],
    "peminat": [
      { "1": [59, 0, 185], "2": [73, 0, 139], "3": [69, 0, 120] },
      { "1": [38, 0, 185], "2": [66, 0, 139], "3": [37, 0, 120] },
      { "1": [39, 0, 185], "2": [35, 0, 139], "3": [27, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [5, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [6, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [6, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      }
    ]
  },
  "1005806": {
    "sekolah": "SMK NEGERI 39",
    "kompetensi": [
      "Teknik Kendaraan Ringan",
      "Teknik Sepeda Motor",
      "Teknik Audio Video",
      "Teknik Elektronika Industri",
      "Teknik Elektronika Komunikasi"
    ],
    "k_kompetensi": [2046, 2047, 2048, 2049, 2601],
    "kapasitas": [
      [[25, 0, 46]],
      [[12, 0, 46]],
      [[27, 0, 46]],
      [[23, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["46.05", "49.35", "47.16"],
      ["45.70", "47.83", "46.61"],
      ["45.62", "48.21", "46.14"],
      ["45.78", "48.71", "46.85"],
      ["45.89", "49.15", "46.88"]
    ],
    "peminat": [
      { "1": [59, 0, 185], "2": [67, 0, 139], "3": [78, 0, 120] },
      { "1": [29, 0, 185], "2": [44, 0, 139], "3": [41, 0, 120] },
      { "1": [56, 0, 185], "2": [66, 0, 139], "3": [47, 0, 120] },
      { "1": [30, 0, 185], "2": [46, 0, 139], "3": [42, 0, 120] },
      { "1": [13, 0, 185], "2": [15, 0, 139], "3": [33, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [3, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [10, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [5, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005807": {
    "sekolah": "SMK NEGERI 40",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2051, 2052, 2053, 2054, 2055],
    "kapasitas": [
      [[11, 0, 46]],
      [[24, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["47.17", "50.49", "48.30"],
      ["46.36", "50.15", "47.61"],
      ["48.56", "50.25", "49.24"],
      ["46.95", "49.94", "48.00"],
      ["47.37", "52.25", "48.83"]
    ],
    "peminat": [
      { "1": [15, 0, 185], "2": [22, 0, 139], "3": [27, 0, 120] },
      { "1": [45, 0, 185], "2": [36, 0, 139], "3": [29, 0, 120] },
      { "1": [40, 0, 185], "2": [39, 0, 139], "3": [31, 0, 120] },
      { "1": [21, 0, 185], "2": [24, 0, 139], "3": [13, 0, 120] },
      { "1": [22, 0, 185], "2": [23, 0, 139], "3": [20, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005808": {
    "sekolah": "SMK NEGERI 41",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2056, 2057, 2058, 2060, 2059],
    "kapasitas": [
      [[22, 0, 46]],
      [[12, 0, 46]],
      [[26, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["45.81", "52.46", "48.52"],
      ["48.87", "52.74", "50.00"],
      ["46.28", "54.47", "48.46"],
      ["45.88", "50.54", "47.23"],
      ["46.62", "50.32", "48.13"]
    ],
    "peminat": [
      { "1": [33, 0, 185], "2": [21, 0, 139], "3": [21, 0, 120] },
      { "1": [42, 0, 185], "2": [31, 0, 139], "3": [33, 0, 120] },
      { "1": [37, 0, 185], "2": [21, 0, 139], "3": [29, 0, 120] },
      { "1": [31, 0, 185], "2": [29, 0, 139], "3": [24, 0, 120] },
      { "1": [33, 0, 185], "2": [26, 0, 139], "3": [19, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005809": {
    "sekolah": "SMK NEGERI 42",
    "kompetensi": [
      "Produksi dan Siaran Program Radio",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2061, 2062, 2063, 2064],
    "kapasitas": [[[13, 0, 46]], [[24, 0, 46]], [[27, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["50.18", "55.91", "51.67"],
      ["51.88", "54.97", "52.69"],
      ["52.21", "54.98", "53.25"],
      ["50.56", "54.94", "51.55"]
    ],
    "peminat": [
      { "1": [43, 0, 185], "2": [50, 0, 139], "3": [38, 0, 120] },
      { "1": [185, 0, 185], "2": [139, 0, 139], "3": [80, 0, 120] },
      { "1": [76, 0, 185], "2": [57, 0, 139], "3": [26, 0, 120] },
      { "1": [82, 0, 185], "2": [80, 0, 139], "3": [68, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [24, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [27, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005810": {
    "sekolah": "SMK NEGERI 43",
    "kompetensi": [
      "Manajemen Logistik",
      "Rekayasa Perangkat Lunak",
      "Teknik Komputer dan Jaringan",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2066, 2069, 2065, 2067, 2068],
    "kapasitas": [
      [[12, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["47.37", "50.95", "48.34"],
      ["47.31", "49.35", "47.99"],
      ["48.28", "51.30", "49.50"],
      ["47.64", "49.59", "48.26"],
      ["47.81", "49.85", "48.42"]
    ],
    "peminat": [
      { "1": [33, 0, 185], "2": [14, 0, 139], "3": [17, 0, 120] },
      { "1": [25, 0, 185], "2": [25, 0, 139], "3": [10, 0, 120] },
      { "1": [40, 0, 185], "2": [22, 0, 139], "3": [24, 0, 120] },
      { "1": [27, 0, 185], "2": [21, 0, 139], "3": [27, 0, 120] },
      { "1": [57, 0, 185], "2": [71, 0, 139], "3": [47, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005811": {
    "sekolah": "SMK NEGERI 44",
    "kompetensi": [
      "Teknik Komputer dan Jaringan",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2070, 2071, 2072, 2073],
    "kapasitas": [[[11, 0, 46]], [[11, 0, 46]], [[27, 0, 46]], [[25, 0, 46]]],
    "rekap": [
      ["45.88", "49.50", "47.29"],
      ["47.83", "50.46", "48.77"],
      ["46.14", "50.48", "47.42"],
      ["46.32", "49.14", "47.10"]
    ],
    "peminat": [
      { "1": [30, 0, 185], "2": [31, 0, 139], "3": [38, 0, 120] },
      { "1": [32, 0, 185], "2": [24, 0, 139], "3": [33, 0, 120] },
      { "1": [51, 0, 185], "2": [35, 0, 139], "3": [41, 0, 120] },
      { "1": [42, 0, 185], "2": [51, 0, 139], "3": [45, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [9, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005812": {
    "sekolah": "SMK NEGERI 45",
    "kompetensi": [
      "Produksi dan Siaran Program Televisi",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2074, 2078, 2075, 2076, 2077],
    "kapasitas": [
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[23, 0, 46]],
      [[26, 0, 46]],
      [[23, 0, 46]]
    ],
    "rekap": [
      ["48.05", "49.80", "48.66"],
      ["49.02", "51.80", "50.22"],
      ["49.51", "52.24", "50.66"],
      ["48.17", "52.54", "49.61"],
      ["48.41", "51.45", "49.41"]
    ],
    "peminat": [
      { "1": [22, 0, 185], "2": [23, 0, 139], "3": [20, 0, 120] },
      { "1": [36, 0, 185], "2": [26, 0, 139], "3": [34, 0, 120] },
      { "1": [85, 0, 185], "2": [90, 0, 139], "3": [68, 0, 120] },
      { "1": [44, 0, 185], "2": [54, 0, 139], "3": [41, 0, 120] },
      { "1": [68, 0, 185], "2": [87, 0, 139], "3": [97, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [7, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [5, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005813": {
    "sekolah": "SMK NEGERI 46",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2079, 2080, 2081, 2082, 2083],
    "kapasitas": [
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[25, 0, 46]],
      [[27, 0, 46]],
      [[23, 0, 46]]
    ],
    "rekap": [
      ["47.33", "52.28", "49.01"],
      ["47.23", "50.38", "48.17"],
      ["48.52", "51.17", "49.55"],
      ["47.30", "51.43", "48.46"],
      ["47.55", "52.63", "48.72"]
    ],
    "peminat": [
      { "1": [36, 0, 185], "2": [21, 0, 139], "3": [23, 0, 120] },
      { "1": [21, 0, 185], "2": [45, 0, 139], "3": [60, 0, 120] },
      { "1": [57, 0, 185], "2": [56, 0, 139], "3": [59, 0, 120] },
      { "1": [29, 0, 185], "2": [52, 0, 139], "3": [45, 0, 120] },
      { "1": [32, 0, 185], "2": [47, 0, 139], "3": [45, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [0, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [9, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [13, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [8, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005814": {
    "sekolah": "SMK NEGERI 47",
    "kompetensi": [
      "Produksi dan Siaran Program Televisi",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2085, 2084, 2086, 2087, 2088],
    "kapasitas": [
      [[13, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[27, 0, 46]],
      [[25, 0, 46]]
    ],
    "rekap": [
      ["46.27", "48.27", "46.94"],
      ["46.43", "49.61", "47.61"],
      ["48.80", "53.52", "49.73"],
      ["46.34", "50.14", "47.45"],
      ["46.80", "49.69", "48.00"]
    ],
    "peminat": [
      { "1": [18, 0, 185], "2": [22, 0, 139], "3": [28, 0, 120] },
      { "1": [26, 0, 185], "2": [22, 0, 139], "3": [32, 0, 120] },
      { "1": [63, 0, 185], "2": [68, 0, 139], "3": [63, 0, 120] },
      { "1": [42, 0, 185], "2": [49, 0, 139], "3": [40, 0, 120] },
      { "1": [61, 0, 185], "2": [71, 0, 139], "3": [58, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [8, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [5, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005815": {
    "sekolah": "SMK NEGERI 48",
    "kompetensi": [
      "Produksi dan Siaran Program Televisi",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail",
      "Bisnis Digital"
    ],
    "k_kompetensi": [2090, 2089, 2091, 2092, 2094, 2093],
    "kapasitas": [
      [[11, 0, 46]],
      [[22, 0, 46]],
      [[11, 0, 46]],
      [[25, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["49.64", "53.56", "51.29"],
      ["48.57", "54.57", "49.83"],
      ["51.07", "53.64", "52.20"],
      ["50.51", "55.57", "52.10"],
      ["49.82", "52.88", "50.47"],
      ["50.26", "52.81", "51.73"]
    ],
    "peminat": [
      { "1": [21, 0, 185], "2": [15, 0, 139], "3": [11, 0, 120] },
      { "1": [56, 0, 185], "2": [35, 0, 139], "3": [31, 0, 120] },
      { "1": [90, 0, 185], "2": [57, 0, 139], "3": [40, 0, 120] },
      { "1": [61, 0, 185], "2": [22, 0, 139], "3": [18, 0, 120] },
      { "1": [18, 0, 185], "2": [24, 0, 139], "3": [22, 0, 120] },
      { "1": [39, 0, 185], "2": [25, 0, 139], "3": [26, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005816": {
    "sekolah": "SMK NEGERI 49",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Logistik",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Layanan Perbankan Syariah",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2095, 2099, 2098, 2101, 2096, 2100, 2097],
    "kapasitas": [
      [[23, 0, 46]],
      [[12, 0, 46]],
      [[11, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]],
      [[13, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["47.54", "51.22", "48.71"],
      ["49.24", "50.90", "49.96"],
      ["50.90", "58.07", "52.38"],
      ["48.97", "52.27", "50.21"],
      ["48.89", "54.80", "50.80"],
      ["48.52", "51.68", "49.58"],
      ["48.91", "52.82", "50.25"]
    ],
    "peminat": [
      { "1": [45, 0, 185], "2": [32, 0, 139], "3": [30, 0, 120] },
      { "1": [27, 0, 185], "2": [28, 0, 139], "3": [31, 0, 120] },
      { "1": [61, 0, 185], "2": [54, 0, 139], "3": [50, 0, 120] },
      { "1": [23, 0, 185], "2": [25, 0, 139], "3": [24, 0, 120] },
      { "1": [21, 0, 185], "2": [36, 0, 139], "3": [27, 0, 120] },
      { "1": [16, 0, 185], "2": [34, 0, 139], "3": [24, 0, 120] },
      { "1": [24, 0, 185], "2": [32, 0, 139], "3": [29, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005817": {
    "sekolah": "SMK NEGERI 50",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2102, 2103, 2104, 2106, 2105],
    "kapasitas": [
      [[11, 0, 46]],
      [[6, 0, 46]],
      [[25, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["48.00", "50.49", "48.90"],
      ["49.95", "53.01", "50.76"],
      ["47.58", "51.69", "49.11"],
      ["48.16", "52.98", "49.40"],
      ["47.65", "50.31", "48.66"]
    ],
    "peminat": [
      { "1": [33, 0, 185], "2": [40, 0, 139], "3": [35, 0, 120] },
      { "1": [45, 0, 185], "2": [65, 0, 139], "3": [60, 0, 120] },
      { "1": [30, 0, 185], "2": [42, 0, 139], "3": [40, 0, 120] },
      { "1": [21, 0, 185], "2": [35, 0, 139], "3": [25, 0, 120] },
      { "1": [26, 0, 185], "2": [50, 0, 139], "3": [43, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [3, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[6, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [9, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005818": {
    "sekolah": "SMK NEGERI 51",
    "kompetensi": [
      "Produksi dan Siaran Program Televisi",
      "Produksi Film",
      "Desain Komunikasi Visual",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2107, 2108, 2109, 2110, 2111, 2113, 2112],
    "kapasitas": [
      [[13, 0, 46]],
      [[11, 0, 46]],
      [[25, 0, 46]],
      [[26, 0, 46]],
      [[12, 0, 46]],
      [[12, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["46.30", "51.49", "48.33"],
      ["47.27", "53.27", "48.80"],
      ["45.86", "50.68", "47.37"],
      ["48.26", "53.92", "50.14"],
      ["46.86", "50.44", "48.46"],
      ["46.95", "52.28", "48.77"],
      ["46.69", "51.93", "47.58"]
    ],
    "peminat": [
      { "1": [18, 0, 185], "2": [20, 0, 139], "3": [20, 0, 120] },
      { "1": [21, 0, 185], "2": [18, 0, 139], "3": [19, 0, 120] },
      { "1": [40, 0, 185], "2": [40, 0, 139], "3": [29, 0, 120] },
      { "1": [51, 0, 185], "2": [44, 0, 139], "3": [72, 0, 120] },
      { "1": [18, 0, 185], "2": [30, 0, 139], "3": [10, 0, 120] },
      { "1": [27, 0, 185], "2": [29, 0, 139], "3": [24, 0, 120] },
      { "1": [32, 0, 185], "2": [32, 0, 139], "3": [19, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [0, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005819": {
    "sekolah": "SMK NEGERI 52",
    "kompetensi": [
      "Desain Pemodelan dan Informasi Bangunan",
      "Desain dan Teknik Furnitur",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan"
    ],
    "k_kompetensi": [2114, 2115, 2116, 2117],
    "kapasitas": [[[24, 0, 46]], [[22, 0, 46]], [[23, 0, 46]], [[22, 0, 46]]],
    "rekap": [
      ["44.77", "48.88", "45.96"],
      ["44.59", "48.84", "45.70"],
      ["45.08", "49.34", "46.61"],
      ["45.43", "52.15", "46.89"]
    ],
    "peminat": [
      { "1": [47, 0, 185], "2": [28, 0, 139], "3": [28, 0, 120] },
      { "1": [48, 0, 185], "2": [39, 0, 139], "3": [32, 0, 120] },
      { "1": [46, 0, 185], "2": [44, 0, 139], "3": [15, 0, 120] },
      { "1": [72, 0, 185], "2": [34, 0, 139], "3": [37, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [1, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [1, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      }
    ]
  },
  "1005820": {
    "sekolah": "SMK NEGERI 53",
    "kompetensi": [
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Pengelasan",
      "Teknik Kendaraan Ringan",
      "Teknik Sepeda Motor",
      "Teknik Audio Video",
      "Teknik Komputer dan Jaringan"
    ],
    "k_kompetensi": [2118, 2119, 2120, 2121, 2122, 2123],
    "kapasitas": [
      [[23, 0, 46]],
      [[25, 0, 46]],
      [[22, 0, 46]],
      [[26, 0, 46]],
      [[26, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["48.64", "51.67", "49.45"],
      ["47.94", "50.12", "48.73"],
      ["48.20", "50.18", "49.19"],
      ["47.70", "50.04", "48.63"],
      ["49.62", "51.92", "50.42"],
      ["51.56", "54.67", "52.38"]
    ],
    "peminat": [
      { "1": [119, 0, 185], "2": [55, 0, 139], "3": [59, 0, 120] },
      { "1": [139, 0, 185], "2": [90, 0, 139], "3": [72, 0, 120] },
      { "1": [108, 0, 185], "2": [104, 0, 139], "3": [60, 0, 120] },
      { "1": [144, 0, 185], "2": [94, 0, 139], "3": [80, 0, 120] },
      { "1": [75, 0, 185], "2": [64, 0, 139], "3": [47, 0, 120] },
      { "1": [170, 0, 185], "2": [103, 0, 139], "3": [106, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [8, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [9, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [9, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005821": {
    "sekolah": "SMK NEGERI 54",
    "kompetensi": [
      "Teknik Pemanasan, Tata Udara, dan Pendinginan",
      "Teknik Kendaraan Ringan",
      "Teknik Komputer dan Jaringan"
    ],
    "k_kompetensi": [2124, 2125, 2126],
    "kapasitas": [[[26, 0, 46]], [[40, 0, 46]], [[26, 0, 46]]],
    "rekap": [
      ["45.27", "48.72", "46.20"],
      ["45.37", "49.46", "46.50"],
      ["46.12", "50.61", "47.61"]
    ],
    "peminat": [
      { "1": [69, 0, 185], "2": [49, 0, 139], "3": [34, 0, 120] },
      { "1": [76, 0, 185], "2": [77, 0, 139], "3": [61, 0, 120] },
      { "1": [41, 0, 185], "2": [48, 0, 139], "3": [55, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [3, 0, 13], "3": [7, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [13, 0, 13], "3": [7, 0, 10] },
        "by-kapasitas": [[40, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [3, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      }
    ]
  },
  "1005822": {
    "sekolah": "SMK NEGERI 55",
    "kompetensi": [
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Kendaraan Ringan",
      "Teknik Sepeda Motor",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [2127, 2128, 2129, 2130],
    "kapasitas": [[[27, 0, 46]], [[25, 0, 46]], [[11, 0, 46]], [[25, 0, 46]]],
    "rekap": [
      ["46.08", "49.94", "47.17"],
      ["46.45", "52.79", "47.77"],
      ["45.91", "47.68", "46.48"],
      ["47.09", "50.77", "48.43"]
    ],
    "peminat": [
      { "1": [63, 0, 185], "2": [44, 0, 139], "3": [32, 0, 120] },
      { "1": [82, 0, 185], "2": [61, 0, 139], "3": [36, 0, 120] },
      { "1": [38, 0, 185], "2": [39, 0, 139], "3": [51, 0, 120] },
      { "1": [41, 0, 185], "2": [33, 0, 139], "3": [46, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [6, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [5, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [6, 0, 43], "2": [3, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [3, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005823": {
    "sekolah": "SMK NEGERI 56",
    "kompetensi": [
      "Desain Pemodelan dan Informasi Bangunan",
      "Teknik Instalasi Tenaga Listrik",
      "Teknik Otomasi Industri",
      "Teknik Pemesinan",
      "Teknik Kendaraan Ringan",
      "Teknik Ototronik",
      "Teknik Mekatronika",
      "Teknik Komputer dan Jaringan",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139],
    "kapasitas": [
      [[11, 0, 46]],
      [[25, 0, 46]],
      [[13, 0, 46]],
      [[26, 0, 46]],
      [[23, 0, 46]],
      [[13, 0, 46]],
      [[26, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]]
    ],
    "rekap": [
      ["46.91", "48.21", "47.35"],
      ["46.48", "48.58", "47.48"],
      ["46.83", "48.44", "47.66"],
      ["46.21", "48.65", "46.90"],
      ["46.29", "51.89", "47.86"],
      ["46.30", "48.42", "47.05"],
      ["46.32", "49.36", "47.26"],
      ["48.68", "51.92", "50.12"],
      ["48.13", "51.66", "48.76"]
    ],
    "peminat": [
      { "1": [23, 0, 185], "2": [22, 0, 139], "3": [23, 0, 120] },
      { "1": [75, 0, 185], "2": [55, 0, 139], "3": [44, 0, 120] },
      { "1": [40, 0, 185], "2": [26, 0, 139], "3": [40, 0, 120] },
      { "1": [53, 0, 185], "2": [65, 0, 139], "3": [60, 0, 120] },
      { "1": [94, 0, 185], "2": [84, 0, 139], "3": [71, 0, 120] },
      { "1": [44, 0, 185], "2": [47, 0, 139], "3": [23, 0, 120] },
      { "1": [44, 0, 185], "2": [50, 0, 139], "3": [44, 0, 120] },
      { "1": [40, 0, 185], "2": [34, 0, 139], "3": [35, 0, 120] },
      { "1": [16, 0, 185], "2": [29, 0, 139], "3": [34, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [6, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [5, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [2, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005824": {
    "sekolah": "SMK NEGERI 57",
    "kompetensi": ["Usaha Layanan Wisata", "Perhotelan", "Kuliner"],
    "k_kompetensi": [2140, 2141, 2142],
    "kapasitas": [[[26, 0, 46]], [[46, 0, 46]], [[46, 0, 46]]],
    "rekap": [
      ["47.28", "50.87", "48.40"],
      ["47.86", "55.10", "49.30"],
      ["47.46", "50.51", "48.83"]
    ],
    "peminat": [
      { "1": [57, 0, 185], "2": [26, 0, 139], "3": [25, 0, 120] },
      { "1": [129, 0, 185], "2": [77, 0, 139], "3": [63, 0, 120] },
      { "1": [116, 0, 185], "2": [77, 0, 139], "3": [62, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [24, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [43, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[46, 0, 43]]
      },
      {
        "by-pilihan": { "1": [43, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[46, 0, 43]]
      }
    ]
  },
  "1005825": {
    "sekolah": "SMK NEGERI 58",
    "kompetensi": [
      "Desain Pemodelan dan Informasi Bangunan",
      "Teknik Fabrikasi Logam dan Manufaktur",
      "Seni Lukis",
      "Desain Komunikasi Visual",
      "Kriya Kreatif Batik dan Tekstil",
      "Kriya Kreatif Logam dan Perhiasan",
      "Kriya Kreatif Kayu dan Rotan"
    ],
    "k_kompetensi": [2143, 2144, 2145, 2146, 2147, 2148, 2149],
    "kapasitas": [
      [[13, 0, 46]],
      [[23, 0, 46]],
      [[13, 0, 46]],
      [[23, 0, 46]],
      [[11, 0, 46]],
      [[11, 0, 46]],
      [[23, 0, 46]]
    ],
    "rekap": [
      ["46.15", "50.95", "47.65"],
      ["45.40", "48.77", "46.73"],
      ["44.79", "50.61", "46.15"],
      ["45.80", "51.97", "47.45"],
      ["44.81", "47.82", "46.04"],
      ["45.25", "48.88", "46.47"],
      ["44.66", "47.84", "45.49"]
    ],
    "peminat": [
      { "1": [21, 0, 185], "2": [25, 0, 139], "3": [17, 0, 120] },
      { "1": [50, 0, 185], "2": [51, 0, 139], "3": [35, 0, 120] },
      { "1": [38, 0, 185], "2": [22, 0, 139], "3": [25, 0, 120] },
      { "1": [41, 0, 185], "2": [53, 0, 139], "3": [57, 0, 120] },
      { "1": [14, 0, 185], "2": [25, 0, 139], "3": [28, 0, 120] },
      { "1": [23, 0, 185], "2": [46, 0, 139], "3": [20, 0, 120] },
      { "1": [48, 0, 185], "2": [32, 0, 139], "3": [44, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [1, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [0, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [3, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [13, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005826": {
    "sekolah": "SMK NEGERI 59",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Bisnis Digital",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2150, 2152, 2151],
    "kapasitas": [[[24, 0, 46]], [[13, 0, 46]], [[13, 0, 46]]],
    "rekap": [
      ["46.16", "48.84", "47.52"],
      ["46.53", "50.79", "47.73"],
      ["47.60", "50.67", "48.43"]
    ],
    "peminat": [
      { "1": [32, 0, 185], "2": [40, 0, 139], "3": [37, 0, 120] },
      { "1": [21, 0, 185], "2": [20, 0, 139], "3": [25, 0, 120] },
      { "1": [45, 0, 185], "2": [46, 0, 139], "3": [49, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [7, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  },
  "1005827": {
    "sekolah": "SMK NEGERI 60",
    "kompetensi": ["Usaha Layanan Wisata", "Perhotelan", "Kuliner"],
    "k_kompetensi": [2153, 2155, 2154],
    "kapasitas": [[[23, 0, 46]], [[23, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["49.07", "52.81", "50.31"],
      ["49.48", "52.95", "50.57"],
      ["48.56", "51.56", "49.89"]
    ],
    "peminat": [
      { "1": [63, 0, 185], "2": [55, 0, 139], "3": [43, 0, 120] },
      { "1": [125, 0, 185], "2": [66, 0, 139], "3": [91, 0, 120] },
      { "1": [85, 0, 185], "2": [65, 0, 139], "3": [50, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [6, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [20, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [1, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005828": {
    "sekolah": "SMK NEGERI 61 (KEPULAUAN SERIBU)",
    "kompetensi": [
      "Nautika Kapal Penangkapan Ikan",
      "Nautika Kapal Niaga",
      "Teknika Kapal Niaga",
      "Kuliner",
      "Agribisnis Perikanan Payau dan Laut"
    ],
    "k_kompetensi": [2156, 2157, 2160, 2158, 2159],
    "kapasitas": [
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]]
    ],
    "rekap": [
      ["41.83", "44.93", "42.96"],
      ["42.84", "46.49", "44.42"],
      ["42.20", "46.73", "43.32"],
      ["42.16", "46.06", "43.53"],
      ["41.03", "43.33", "41.72"]
    ],
    "peminat": [
      { "1": [18, 0, 185], "2": [11, 0, 139], "3": [9, 0, 120] },
      { "1": [21, 0, 185], "2": [12, 0, 139], "3": [6, 0, 120] },
      { "1": [14, 0, 185], "2": [18, 0, 139], "3": [12, 0, 120] },
      { "1": [16, 0, 185], "2": [8, 0, 139], "3": [7, 0, 120] },
      { "1": [15, 0, 185], "2": [11, 0, 139], "3": [6, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [2, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [6, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005829": {
    "sekolah": "SMK NEGERI 62",
    "kompetensi": [
      "Desain Komunikasi Visual",
      "Perhotelan",
      "Manajemen Perkantoran",
      "Akuntansi",
      "Bisnis Retail"
    ],
    "k_kompetensi": [2161, 2162, 2163, 2164, 2165],
    "kapasitas": [
      [[13, 0, 46]],
      [[13, 0, 46]],
      [[12, 0, 46]],
      [[13, 0, 46]],
      [[13, 0, 46]]
    ],
    "rekap": [
      ["46.08", "50.65", "47.87"],
      ["47.16", "50.84", "48.77"],
      ["48.56", "56.11", "50.76"],
      ["46.10", "51.83", "48.26"],
      ["45.89", "53.46", "47.44"]
    ],
    "peminat": [
      { "1": [24, 0, 185], "2": [16, 0, 139], "3": [15, 0, 120] },
      { "1": [52, 0, 185], "2": [38, 0, 139], "3": [34, 0, 120] },
      { "1": [40, 0, 185], "2": [24, 0, 139], "3": [20, 0, 120] },
      { "1": [31, 0, 185], "2": [19, 0, 139], "3": [14, 0, 120] },
      { "1": [25, 0, 185], "2": [23, 0, 139], "3": [24, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [4, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [0, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [4, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  },
  "1005830": {
    "sekolah": "SMK NEGERI 63",
    "kompetensi": [
      "Agribisnis Tanaman Pangan dan Hortikultura",
      "Agribisnis Perbenihan Tanaman",
      "Agribisnis Lanskap dan Pertamanan",
      "Agribisnis Pengolahan Hasil Pertanian"
    ],
    "k_kompetensi": [2166, 2167, 2168, 2169],
    "kapasitas": [[[40, 0, 46]], [[12, 0, 46]], [[26, 0, 46]], [[27, 0, 46]]],
    "rekap": [
      ["44.88", "49.28", "46.39"],
      ["44.85", "53.24", "46.15"],
      ["44.89", "50.87", "46.13"],
      ["45.30", "53.57", "46.95"]
    ],
    "peminat": [
      { "1": [70, 0, 185], "2": [40, 0, 139], "3": [47, 0, 120] },
      { "1": [36, 0, 185], "2": [40, 0, 139], "3": [29, 0, 120] },
      { "1": [38, 0, 185], "2": [46, 0, 139], "3": [45, 0, 120] },
      { "1": [49, 0, 185], "2": [32, 0, 139], "3": [31, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [23, 0, 43], "2": [7, 0, 13], "3": [10, 0, 10] },
        "by-kapasitas": [[40, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [2, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [21, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      }
    ]
  },
  "1005831": {
    "sekolah": "SMK NEGERI 64",
    "kompetensi": ["Rekayasa Perangkat Lunak", "Desain Komunikasi Visual"],
    "k_kompetensi": [2170, 2171],
    "kapasitas": [[[26, 0, 46]], [[12, 0, 46]]],
    "rekap": [
      ["45.16", "50.97", "46.42"],
      ["45.67", "51.63", "46.98"]
    ],
    "peminat": [
      { "1": [51, 0, 185], "2": [25, 0, 139], "3": [32, 0, 120] },
      { "1": [24, 0, 185], "2": [36, 0, 139], "3": [27, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [19, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      }
    ]
  },
  "1005832": {
    "sekolah": "SMK NEGERI 65",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Produksi Film",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [2172, 2174, 2173],
    "kapasitas": [[[23, 0, 46]], [[27, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["46.46", "50.73", "47.43"],
      ["46.34", "49.28", "47.35"],
      ["46.74", "49.43", "47.84"]
    ],
    "peminat": [
      { "1": [53, 0, 185], "2": [34, 0, 139], "3": [42, 0, 120] },
      { "1": [36, 0, 185], "2": [23, 0, 139], "3": [42, 0, 120] },
      { "1": [29, 0, 185], "2": [41, 0, 139], "3": [36, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [3, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [3, 0, 13], "3": [10, 0, 10] },
        "by-kapasitas": [[27, 0, 43]]
      },
      {
        "by-pilihan": { "1": [12, 0, 43], "2": [6, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005833": {
    "sekolah": "SMK NEGERI 66",
    "kompetensi": ["Usaha Layanan Wisata", "Perhotelan", "Kuliner"],
    "k_kompetensi": [2175, 2176, 2177],
    "kapasitas": [[[11, 0, 46]], [[22, 0, 46]], [[34, 0, 46]]],
    "rekap": [
      ["46.15", "50.02", "47.07"],
      ["46.76", "52.40", "48.23"],
      ["45.85", "51.91", "47.22"]
    ],
    "peminat": [
      { "1": [28, 0, 185], "2": [21, 0, 139], "3": [21, 0, 120] },
      { "1": [53, 0, 185], "2": [36, 0, 139], "3": [40, 0, 120] },
      { "1": [45, 0, 185], "2": [46, 0, 139], "3": [35, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [3, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [18, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[22, 0, 43]]
      },
      {
        "by-pilihan": { "1": [22, 0, 43], "2": [9, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[34, 0, 43]]
      }
    ]
  },
  "1005834": {
    "sekolah": "SMK NEGERI 67",
    "kompetensi": ["Animasi", "Desain Komunikasi Visual"],
    "k_kompetensi": [2178, 2179],
    "kapasitas": [[[12, 0, 46]], [[38, 0, 46]]],
    "rekap": [
      ["44.66", "49.53", "45.80"],
      ["44.85", "48.86", "46.42"]
    ],
    "peminat": [
      { "1": [24, 0, 185], "2": [20, 0, 139], "3": [12, 0, 120] },
      { "1": [51, 0, 185], "2": [37, 0, 139], "3": [27, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [29, 0, 43], "2": [7, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[38, 0, 43]]
      }
    ]
  },
  "1005835": {
    "sekolah": "SMK NEGERI 68",
    "kompetensi": [
      "Teknik Pengelasan",
      "Teknik Fabrikasi Logam dan Manufaktur"
    ],
    "k_kompetensi": [2180, 2181],
    "kapasitas": [[[23, 0, 46]], [[25, 0, 46]]],
    "rekap": [
      ["44.76", "48.83", "45.91"],
      ["44.70", "49.43", "45.90"]
    ],
    "peminat": [
      { "1": [67, 0, 185], "2": [42, 0, 139], "3": [24, 0, 120] },
      { "1": [42, 0, 185], "2": [57, 0, 139], "3": [35, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [17, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [11, 0, 43], "2": [9, 0, 13], "3": [5, 0, 10] },
        "by-kapasitas": [[25, 0, 43]]
      }
    ]
  },
  "1005836": {
    "sekolah": "SMK NEGERI 69",
    "kompetensi": [
      "Teknik Ototronik",
      "Teknik Mekatronika",
      "Sistem Informasi, Jaringan dan Aplikasi"
    ],
    "k_kompetensi": [2182, 2183, 2184],
    "kapasitas": [[[23, 0, 46]], [[26, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["47.28", "50.53", "48.90"],
      ["47.18", "50.90", "48.40"],
      ["49.04", "52.52", "50.35"]
    ],
    "peminat": [
      { "1": [93, 0, 185], "2": [51, 0, 139], "3": [41, 0, 120] },
      { "1": [54, 0, 185], "2": [67, 0, 139], "3": [39, 0, 120] },
      { "1": [56, 0, 185], "2": [57, 0, 139], "3": [58, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [7, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [8, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [8, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005837": {
    "sekolah": "SMK NEGERI 70",
    "kompetensi": ["Perhotelan", "Kuliner", "Desain dan Produksi Busana"],
    "k_kompetensi": [2185, 2186, 2187],
    "kapasitas": [[[11, 0, 46]], [[8, 0, 46]], [[11, 0, 46]]],
    "rekap": [
      ["48.48", "50.81", "49.50"],
      ["49.20", "51.79", "50.02"],
      ["47.06", "48.94", "47.84"]
    ],
    "peminat": [
      { "1": [42, 0, 185], "2": [32, 0, 139], "3": [27, 0, 120] },
      { "1": [36, 0, 185], "2": [32, 0, 139], "3": [25, 0, 120] },
      { "1": [21, 0, 185], "2": [17, 0, 139], "3": [20, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [8, 0, 43], "2": [3, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [5, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[8, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [1, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      }
    ]
  },
  "1005838": {
    "sekolah": "SMK NEGERI 71",
    "kompetensi": [
      "Rekayasa Perangkat Lunak",
      "Animasi",
      "Desain Komunikasi Visual"
    ],
    "k_kompetensi": [2189, 2190, 2188],
    "kapasitas": [[[23, 0, 46]], [[13, 0, 46]], [[23, 0, 46]]],
    "rekap": [
      ["47.04", "52.00", "48.54"],
      ["47.00", "50.56", "48.52"],
      ["47.03", "50.89", "47.98"]
    ],
    "peminat": [
      { "1": [48, 0, 185], "2": [67, 0, 139], "3": [66, 0, 120] },
      { "1": [26, 0, 185], "2": [29, 0, 139], "3": [30, 0, 120] },
      { "1": [38, 0, 185], "2": [58, 0, 139], "3": [54, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [2, 0, 13], "3": [7, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [2, 0, 13], "3": [1, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [5, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      }
    ]
  },
  "1005839": {
    "sekolah": "SMK NEGERI 72",
    "kompetensi": [
      "Teknik Jaringan Tenaga Listrik",
      "Teknik Pemanasan, Tata Udara, dan Pendinginan"
    ],
    "k_kompetensi": [2191, 2192],
    "kapasitas": [[[26, 0, 46]], [[26, 0, 46]]],
    "rekap": [
      ["47.61", "51.56", "48.78"],
      ["48.06", "50.24", "48.89"]
    ],
    "peminat": [
      { "1": [59, 0, 185], "2": [113, 0, 139], "3": [102, 0, 120] },
      { "1": [69, 0, 185], "2": [87, 0, 139], "3": [82, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [10, 0, 13], "3": [6, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      },
      {
        "by-pilihan": { "1": [15, 0, 43], "2": [4, 0, 13], "3": [7, 0, 10] },
        "by-kapasitas": [[26, 0, 43]]
      }
    ]
  },
  "1005840": {
    "sekolah": "SMK NEGERI 73",
    "kompetensi": ["Usaha Layanan Wisata", "Perhotelan", "Kuliner"],
    "k_kompetensi": [2193, 2194, 2195],
    "kapasitas": [[[23, 0, 46]], [[23, 0, 46]], [[24, 0, 46]]],
    "rekap": [
      ["49.99", "53.93", "50.83"],
      ["50.34", "52.90", "51.24"],
      ["49.84", "52.42", "50.85"]
    ],
    "peminat": [
      { "1": [80, 0, 185], "2": [65, 0, 139], "3": [76, 0, 120] },
      { "1": [87, 0, 185], "2": [117, 0, 139], "3": [120, 0, 120] },
      { "1": [80, 0, 185], "2": [75, 0, 139], "3": [79, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [9, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [14, 0, 43], "2": [6, 0, 13], "3": [3, 0, 10] },
        "by-kapasitas": [[23, 0, 43]]
      },
      {
        "by-pilihan": { "1": [16, 0, 43], "2": [4, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[24, 0, 43]]
      }
    ]
  },
  "1005841": {
    "sekolah": "SMK NEGERI 74",
    "kompetensi": ["Seni Musik", "Seni Tari", "Seni Karawitan", "Seni Teater"],
    "k_kompetensi": [2196, 2197, 2198, 2199],
    "kapasitas": [[[12, 0, 46]], [[11, 0, 46]], [[13, 0, 46]], [[13, 0, 46]]],
    "rekap": [
      ["44.82", "48.01", "45.73"],
      ["45.63", "50.29", "46.87"],
      ["44.47", "47.68", "45.14"],
      ["44.93", "47.90", "45.86"]
    ],
    "peminat": [
      { "1": [27, 0, 185], "2": [16, 0, 139], "3": [26, 0, 120] },
      { "1": [20, 0, 185], "2": [6, 0, 139], "3": [18, 0, 120] },
      { "1": [38, 0, 185], "2": [20, 0, 139], "3": [17, 0, 120] },
      { "1": [17, 0, 185], "2": [19, 0, 139], "3": [21, 0, 120] }
    ],
    "diterima": [
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [1, 0, 13], "3": [4, 0, 10] },
        "by-kapasitas": [[12, 0, 43]]
      },
      {
        "by-pilihan": { "1": [10, 0, 43], "2": [1, 0, 13], "3": [0, 0, 10] },
        "by-kapasitas": [[11, 0, 43]]
      },
      {
        "by-pilihan": { "1": [7, 0, 43], "2": [4, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      },
      {
        "by-pilihan": { "1": [9, 0, 43], "2": [2, 0, 13], "3": [2, 0, 10] },
        "by-kapasitas": [[13, 0, 43]]
      }
    ]
  }
}

jakarta_timur_schools = [school for school in sch_list if school["k_kota"] == 20106]

seleksi = "https://spmb.jakarta.go.id/seleksi/kjp/smk/1-{school_id}-{kompetensi}.json"
jakarta_timur_schools_hasil_seleksi = [
  {
    "school_id": int(key),
    "nama": value["sekolah"],
    "k_kompetensi": value["k_kompetensi"],
    "seleksi_url": [seleksi.format(school_id=key, kompetensi=k) for k in value["k_kompetensi"]]
    } for key, value in sch_detail_list.items() if value["sekolah"] in [school["nama"] for school in jakarta_timur_schools]
]

hasil = []

for school in jakarta_timur_schools_hasil_seleksi:
    data_sekolah = {
        "school_id": school["school_id"],
        "nama": school["nama"],
        "hasil": []
    }

    for url in school["seleksi_url"]:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data_sekolah["hasil"].append({
                "url": url,
                "data": response.json()
            })

        except Exception as e:
            data_sekolah["hasil"].append({
                "url": url,
                "error": str(e)
            })
        time.sleep(3)

    hasil.append(data_sekolah)

with open(
    "hasil_seleksi_jakarta_timur.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        hasil,
        f,
        ensure_ascii=False,
        indent=2
    )