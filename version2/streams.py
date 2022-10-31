# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas imperdiet massa vel nulla cursus, eget finibus tellus rhoncus. Donec molestie elit eu erat blandit, ac consequat turpis ultrices. Nunc vitae magna nisi. Vestibulum bibendum dignissim nisl, in pretium ante pharetra a. Quisque magna felis, blandit volutpat consectetur id, blandit sed enim. Aenean vestibulum at turpis laoreet semper. Nunc egestas libero eget orci egestas, ac sollicitudin mauris auctor. Proin elit ipsum, scelerisque sit amet mi vitae, tempor porttitor ligula. Suspendisse rhoncus lectus est, tincidunt accumsan odio pulvinar ut. Ut fringilla tristique ex et lacinia. Vivamus nunc quam, pellentesque a justo vitae, dictum commodo tortor. Proin condimentum efficitur quam placerat interdum. Sed elementum vitae eros vel fringilla. Quisque a nulla efficitur, bibendum magna id, vestibulum lacus."
# x = text.split()

# print(x)

class Stream:

    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas imperdiet massa vel nulla cursus, eget finibus tellus rhoncus. Donec molestie elit eu erat blandit, ac consequat turpis ultrices. Nunc vitae magna nisi. Vestibulum bibendum dignissim nisl, in pretium ante pharetra a. Quisque magna felis, blandit volutpat consectetur id, blandit sed enim. Aenean vestibulum at turpis laoreet semper. Nunc egestas libero eget orci egestas, ac sollicitudin mauris auctor. Proin elit ipsum, scelerisque sit amet mi vitae, tempor porttitor ligula. Suspendisse rhoncus lectus est, tincidunt accumsan odio pulvinar ut. Ut fringilla tristique ex et lacinia. Vivamus nunc quam, pellentesque a justo vitae, dictum commodo tortor. Proin condimentum efficitur quam placerat interdum. Sed elementum vitae eros vel fringilla. Quisque a nulla efficitur, bibendum magna id, vestibulum lacus."
    pirate = "Well blow me down? That’s some treasure chest you’ve got there. The existence of the sea means the existence of pirates. Merchant and pirate were for a long period one and the same person. Even today mercantile morality is really nothing but a refinement of piratical morality. Damnation seize my soul if I give you quarters, or take any from you."

    @staticmethod
    def stream_getter(stream:str)->str:
        return Stream.stream

    @staticmethod
    def stream_to_list(stream:str)->list:
        stream_list = stream.split()
        return stream_list


# print(Stream.stream_to_list(Stream.lorem))
# print(Stream.stream_to_list(Stream.pirate))


    