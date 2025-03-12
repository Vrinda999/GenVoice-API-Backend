def get_blueprints():
    from .clinicians import clinician_bp
    from .cases import case_bp

    return [
        (clinician_bp, '/clinicians'),
        (case_bp, '/cases')
    ]