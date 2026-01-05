# CSV -> Avro converter

This small script reads a CSV file, infers a simple Avro schema, writes an Avro file, and reads it back to show sample records.

Files added:

- `csv_to_avro.py` - main script
- `requirements.txt` - python deps (pandas, fastavro)

Quick start (macOS / zsh):

1. Create a virtualenv (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install deps:

```bash
pip install -r "bitcoin_price_Training - Training.csv"/../requirements.txt
```

3. Run the converter (example):

```bash
python3 "csv_to_avro.py" \
  --input "bitcoin_price_Training - Training.csv" \
  --output bitcoin.avro \
  --schema-out schema.json
```

This will write `bitcoin.avro` and print a small sample of rows read back from the Avro file.

Notes:
- Schema inference is basic: ints->long, floats->double, bool->boolean, datetimes->string, else string.
- Nullable columns become Avro unions ["null", type] with default null.
