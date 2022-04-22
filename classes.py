class Television:
    """
    A class representing details of a function for a remote linked to a Television
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self, channel=0, volume=0, power: False) -> None:
        """
        Constructor to create initial state of the Television object
        :param channel: Television's current channel
        :param volume: Television's current volume
        :param power: Television's current power state
        """
        
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__power = False 

    def power(self) -> None:
        """
        Method to turn Television on if off, or off if on
        :param power:  Television's current power state
        """
    
        if self.__power == False:
            self.__power = True
        elif self.__power == True:
            self.__power = False

    def channel_up(self) -> None:
        """
        Method to change the Television's channel up a channel
        :param power:  Television's current power state
        :param channel: Television's channel
        """
       
        if self.__power == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        

    def channel_down(self) -> None:
        """
        Method to change the Television's channel down a channel
        :param power:  Television's current power state
        :param channel: Television's channel
        """
       
        if self.__power == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        

    def volume_up(self) -> None:
        """
        Method to change the Television's volume up a level
        :param power:  Television's current power state
        :param Volume: Television's volume
        """
       
        if self.__power == True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume += 0
            else:
                self.__volume += 1
        

    def volume_down(self) -> None:
        """
        Method to change the Television's volume down a level
        :param power:  Television's current power state
        :param Volume: Television's volume
        """
       
        if self.__power == True:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume -= 0
            else:
                self.__volume -= 1
        

    def __str__(self) -> str:
        """
        Method to change the Television's volume up a level
        :return: Final state of Television
        """
        
        return f'TV status: Is on = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}'
