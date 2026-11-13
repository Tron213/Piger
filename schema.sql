CREATE TABLE IF NOT EXISTS monitors(
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    host TEXT NOT NULL,
    enabled BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS ping_results(
    uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    monitor_id UUID REFERENCES monitors(uuid) NOT NULL,
    success BOOLEAN NOT NULL,
    ms BIGINT default NULL,
    checked_at TIMESTAMPTZ default NOW() NOT NULL
);
CREATE UNIQUE INDEX AK_monitors_ping ON ping_results (monitor_id, checked_at);