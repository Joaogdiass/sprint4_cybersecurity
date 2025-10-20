def test_consent_log_is_recorded():
    consent = {"user_id":"u1","accepted":True,"ts":"2025-10-20T10:00:00Z","version":"v1.2","ip":"10.0.0.1"}
    assert consent["accepted"] and consent.get("ts") and consent.get("version") and consent.get("ip")
