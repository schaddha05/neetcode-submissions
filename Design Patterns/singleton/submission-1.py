class Singleton:
    _unique_instance = None 
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton, cls).__new__(cls)
            cls._unique_instance.getInstance()
    
        return cls._unique_instance

    def getInstance(self):
        self.value = None

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
       