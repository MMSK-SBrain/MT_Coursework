-- The generation log is append-only: provenance and cost records are never changed or removed.
CREATE OR REPLACE FUNCTION generation_log_no_change() RETURNS trigger AS $$
BEGIN
  RAISE EXCEPTION 'generation_log is append-only';
END;
$$ LANGUAGE plpgsql;
--> statement-breakpoint
CREATE TRIGGER generation_log_append_only
  BEFORE UPDATE OR DELETE ON generation_log
  FOR EACH ROW EXECUTE FUNCTION generation_log_no_change();
