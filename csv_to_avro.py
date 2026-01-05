import sys
import csv
from fastavro import writer, reader


def make_schema(fieldnames):
    fields = []
    for n in fieldnames:
        name = n.strip().replace(" ", "_")
        fields.append({"name": name, "type": ["null", "string"], "default": None})
    return {"name": "Record", "type": "record", "fields": fields}


def write_avro(csv_path, avro_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        rdr = csv.DictReader(f)
        schema = make_schema(rdr.fieldnames)
        records = [r for r in rdr]

    # fastavro writes records to a binary avro file
    with open(avro_path, 'wb') as out:
        writer(out, schema, records)


def read_avro(avro_path, max_rows=5):
    with open(avro_path, 'rb') as fo:
        for i, rec in enumerate(reader(fo)):
            print(rec)
            if i + 1 >= max_rows:
                break


def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_to_avro.py <input.csv> <output.avro>")
        sys.exit(1)

    csv_path = sys.argv[1]
    avro_path = sys.argv[2]

    print(f"Reading CSV: {csv_path}")
    write_avro(csv_path, avro_path)
    print(f"Wrote Avro: {avro_path}\nReading back (first 5 rows):")
    read_avro(avro_path)


if __name__ == '__main__':
    main()
