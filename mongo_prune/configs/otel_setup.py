import os
import logging
import uptrace


def setup_otel_logging() -> None:
    dsn_value: str | None = os.getenv("OTEL_DSN_VALUE")
    if not dsn_value:
        raise ValueError("OTEL_DSN_VALUE not found in environment")

    uptrace.configure_opentelemetry(
        dsn=dsn_value,
        service_name="mongo_prune",
        service_version="1.0.0",
        logging_level=logging.INFO,  # debug is lowest, need set in main too
    )
