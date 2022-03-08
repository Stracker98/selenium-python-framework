import time
import random,string
import logging
import traceback
import utilities.custom_logger as cl

class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self,sec,info=""):
        if info is not None:
            self.log.info("wait::"+str(sec)+"seconds for"+info)
        try:
            time.sleep(3)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumberic(self,length,type='letters'):

        alpha_num = ""
        if type == 'lower':
            case = string.ascii_lowercase
        elif type =='upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters+ string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))
    def getUniqueName(self,charcount=10):
        return self.getAlphaNumberic(charcount,'lower')
    def getUniqueNameList(self,listsize=5,itemLength=None):

        namelist = []
        for i in range(0,listsize):
            namelist.append(self.getUniqueName(itemLength[i]))
            return namelist

    def verifyTextContains(self,actualText,expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True
