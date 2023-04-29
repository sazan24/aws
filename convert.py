import json, csv
import boto3

for val in ["usd", "eur"]:
    json_file = f"{val}_exchange_rates.json"
    # Open the JSON file and load the data
    with open(json_file, "r") as json_filepath:
        data = json.load(json_filepath)

    csv_file = f"{val}_exchange_rates.csv"
    # Create the CSV file and write the data
    with open(csv_file, "w", newline="") as csv_filepath:
        writer = csv.writer(csv_filepath)

        # Write the headers
        headers = list(data[0].keys())
        writer.writerow(headers)

        # Write the data
        for row in data:
            writer.writerow(list(row.values()))

    # Open a connection with Amazon S3
    s3 = boto3.resource("s3")

    # Upload the CSV file to S3
    s3.Bucket("fightingmyself").upload_file(csv_file, csv_file)
