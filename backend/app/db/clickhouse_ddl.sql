CREATE DATABASE IF NOT EXISTS amlip_analytics;

CREATE TABLE IF NOT EXISTS amlip_analytics.transactions
(
    transaction_id UUID,
    timestamp DateTime64(3, 'UTC'),

    account_from String,
    account_to String,
    customer_from_id String,
    customer_to_id String,

    amount Decimal64(4),
    currency LowCardinality(String),
    amount_usd Decimal64(4),

    payment_method LowCardinality(String),
    ip_address String,
    device_id String,
    location LowCardinality(String),

    risk_score Float32,
    is_flagged UInt8 DEFAULT 0,

    created_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(created_at)
PARTITION BY toYYYYMM(timestamp)
PRIMARY KEY (timestamp, account_from, account_to)
ORDER BY (timestamp, account_from, account_to, transaction_id);
