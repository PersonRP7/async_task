
class StreamOperators:

    # @staticmethod
    # def length_comparison(**kwargs):
    #     for kwarg in kwargs:
    #         print(kwarg)

    @staticmethod
    def length_comparison(**kwargs):
        for key, value in kwargs.items():
            print(f"{key} : {value}")