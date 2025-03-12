'''
This function helps modularise the code and keeps it clean.
This is where all the routes would be indexed. This enables easy scalability and maintenance.
'''

def get_blueprints():
    from .clinicians import clinician_bp
    from .cases import case_bp

    return [
        (clinician_bp, '/clinicians'),
        (case_bp, '/cases')
    ]