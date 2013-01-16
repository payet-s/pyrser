# ------------------------------------------------------------------------------
# unit tests
# ------------------------------------------------------------------------

if __name__ == '__main__':

    import unittest
    from unit_tests.no_depth_generation import generatedCode as NoDepthGeneration
    from unit_tests.multi_generation import generatedCode as MultiDepthGeneration
    from unit_tests.rule_directives import generatedCode as RuleDirective
    from unit_tests.capture import generatedCode as CaptureGeneration
    from unit_tests.composition import generatedCode as CompositionGeneration
    from unit_tests.inheritance import generatedCode as InheritanceGeneration
    from unit_tests.hooks import GenericHookTests

    unittest.main()
