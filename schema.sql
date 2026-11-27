CREATE TABLE IF NOT EXISTS monitors(
    uuid UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    host TEXT NOT NULL,
    enabled BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS ping_results(
    uuid UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    monitor_id UUID REFERENCES monitors(uuid) NOT NULL,
    success BOOLEAN NOT NULL,
    ms DOUBLE PRECISION default NULL,
    checked_at TIMESTAMPTZ default NOW() NOT NULL
);
CREATE UNIQUE INDEX AK_monitors_ping ON ping_results (monitor_id, checked_at);