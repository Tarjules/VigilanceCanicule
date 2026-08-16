from Source.ImportJson import ImportJson


link = ImportJson.construct_url(2025, 6, 12)
ImportJson.import_file(link, "Data", "test.json")
