def test_imports():
    """
    Make sure all stub modules import without crashing
    """
    from wa_leg_api import (  # noqa
        amendment,
        committee,
        committeeaction,
        committeemeeting,
        legislation,
        legislativedocument,
        rcwciteaffected,
        sessionlaw,
        sponsor,
    )
