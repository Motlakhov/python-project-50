import yaml
import json

def parse_file(filepath):
	if filepath.endswith == 'json':
		return file1 = json.load(open(file_path1))
  	file2 = json.load(open(file_path2))
	if filepath.endswith == 'yml', 'yaml':
		return file1 = yaml.safe_load(open(file_path1))
        file2 = yaml.safe_load(open(file_path2))
