import yaml
import json

def parse_file(filepath):
  if filepath.endswith == 'json':
    file = json.load(open(filepath))
  elif filepath.endswith == 'yml' or 'yaml':
    file = yaml.safe_load(open(filepath))
  return file