import math

class Measurement:
    """
    Form a number with an uncertainty.

    Note: This class does not implement many features
    but rather is a test class for uncertainties

    nominal \u00B1 value

    Keyword arguments:
    value -- the nominal component
    error -- the uncertainty component

    """


    def __init__(self,value,error):
        """Initialise the nominal value and the uncertainty
        of the Measurement

        x = Measurement(value,error)

        """

        self.value = value
        self.error = error

    def __eq__(self, other):
        return (self.value == other.value) and (self.error == other.error)


    def __add__(self,other):
        """
        Add two Measurements together

        Parameters:
        argument1 (Measurement): nominal \u00B1 uncertainty
        argument2 (Measurement): nominal \u00B1 uncertainty

        Returns:
        Measurement: Return nominal1 + nominal2 in nominal
                     Return uncertainty in quadrature.
        """
        total_value = self.value + other.value
        total_error = math.sqrt(self.error**2 + other.error**2)
        return Measurement(total_value,total_error )

    def __sub__(self,other):
        """
        Subtract two Measurements

        Parameters:
        argument1 (Measurement): nominal \u00B1 uncertainty
        argument2 (Measurement): nominal \u00B1 uncertainty

        Returns:
        Measurement: Return nominal1 - nominal2 in nominal
                     Return uncertainty in quadrature.
        """

        total_value = self.value - other.value
        total_error = math.sqrt(self.error**2 + other.error**2)

        return Measurement(total_value,total_error)

    def __mul__(self,other):
        """
        Multiply two Measurements together

        Parameters:
        argument1 (Measurement): nominal \u00B1 uncertainty
        argument2 (Measurement): nominal \u00B1 uncertainty

        Returns:
        Measurement: Return nominal1 * nominal2 in nominal
                     Return sqrt( nom2**2*unc1**2 + nom1**2*unc2**2).
        """

        total_value = self.value*other.value
        total_error = math.sqrt((other.value**2)*(self.error**2) + (self.value**2)*(other.error**2))

        return Measurement(total_value,total_error )

    def __truediv__(self,other):
        """
        Divide two Measurements together

        Parameters:
        argument1 (Measurement): nominal \u00B1 uncertainty
        argument2 (Measurement): nominal \u00B1 uncertainty

        Returns:
        Measurement: Return nominal1/nominal2 in nominal
                     Return uncertainty propogated for a/b.
        """

        if other.value == 0.0: raise ZeroDivisionError("Division by Zero error!")

        total_value = self.value/other.value
        total_error = math.sqrt(( (1/other.value)**2)*(self.error**2) + (self.value/other.value/other.value)**2*(other.error**2))
        return Measurement(total_value,total_error)

    def __repr__(self):
        """
        Return representation of Measurement
        Returns: value \u00B1 error
        """
        return str(self.value) +"\u00B1" + str(self.error)



def main():
    """
    Demonstrate the functionality of the Measurement class.

    """
    x = Measurement(1,1)
    y = Measurement(2,2)
    z = Measurement(3,3)

    print("===============================")
    #help(Measurement)
    print("===============================")
    print("x")
    print(x)
    print("y")
    print(y)
    print("z")
    print(z)
    print("===============================")

    print("addition")
    print(x+y)
    print("subtract")
    print(x-y)
    print("multiplication")
    print(x*y)
    print("division")
    print(x/y)
    print("===============================")

    print("x/y*z")
    print(x/y*z)
    print("===============================")


if __name__ == "__main__":
    main()
