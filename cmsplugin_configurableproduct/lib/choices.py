class DynamicChoice(object):
    """
    Trivial example of creating a dynamic choice
    """

    def __iter__(self, *args, **kwargs):
        for choice in self.generate():
            if hasattr(choice,'__iter__'):
                yield (choice[0], choice[1])
            else:
                yield choice, choice

    def __init__(self, *args, **kwargs):
        """
        If you do it here it is only initialized once. Then just return generated.
        """
        import random
        self.generated = [random.randint(1,100) for i in range(10)]

    def generate(self, *args, **kwargs):
        """
        If you do it here it is  initialized every time the iterator is used.
        """
        import random
        return [random.randint(1,100) for i in range(10)]
