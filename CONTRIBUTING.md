# Contributing

Contributions should keep the project reproducible, safe to publish, and easy to validate.

## Workflow

1. Create a focused branch.
2. Make the smallest useful change.
3. Run the test suite:

```bash
python -m unittest discover -s tests -v
```

4. Run the demo:

```bash
python src/fusion_demo.py examples/events.json
```

5. Confirm no credentials, private telemetry, or confidential evidence are included.
6. Open a pull request describing what changed and how it was validated.

## Documentation changes

When changing architecture, feature definitions, thresholds, or deployment assumptions, update the relevant documentation in `docs/` in the same change.

## Code style

Prefer small functions, explicit JSON schemas/fields, deterministic examples, and standard-library dependencies where possible.
