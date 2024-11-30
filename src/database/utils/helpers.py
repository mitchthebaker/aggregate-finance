from datetime import date

def convert_dates_to_strings(a_dict):
  """
  Recursively convert all datetime.date objects in a dictionary to strings.
  """
  for key, value in a_dict.items():
    if isinstance(value, date):
      a_dict[key] = value.isoformat()
    elif isinstance(value, dict):
      convert_dates_to_strings(value)
    elif isinstance(value, list):
      for item in value:
        if isinstance(item, dict):
          convert_dates_to_strings(item)

def convert_arbitrary_type_to_dict(a_list):
  dictionaries = [dictionary.to_dict() for dictionary in a_list]
  for a_dict in dictionaries:
    a_dict['_id'] = a_dict['transaction_id']
    convert_dates_to_strings(a_dict)
  return dictionaries

def assign_document_id(a_list, id_name):
  for a_dict in a_list:
    a_dict['_id'] = a_dict[id_name]
