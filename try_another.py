# import openpyxl
# path = "C://Users/Ratul Hasan/Desktop/Selenium/keyword.xlsx"
# wb = openpyxl.load_workbook(path)
# sheet = wb.active
# rows = sheet.max_row
# clos = sheet.max_column
# print(rows,clos)

# for r in range(1, rows+1):
#     for c in range(1, clos+1):
#         print(sheet.cell(row=r, column=c).value, end="   ")

# java code
# @Test(dataProvider = "ratul")
# public void ratulwork(String device) throws InterruptedException
# 	{
# 		System.out.println("  Institue Name : "+device);
		
# 		//WebDriver driver = new ChromeDriver();
		
# 		System.setProperty("web.chrome.driver", "C://Drivers/chromedriver_win32/chromedriver.exe/");
		 
# 		 WebDriver driver = new ChromeDriver();
		
# 		  driver.get("www.amazon.in");
		   
# 		  driver.manage().window().maximize();
		  
# 		  Thread.sleep(1000);
		  
# 		 // driver.findElement(By.xpath("//*[@id=\"tsf\"]/div[1]/div[1]/div[2]/div/div[2]/input")).sendKeys(instiute);
		 
# 		 // driver.findElement(By.id("twotabsearchtextbox")).sendKeys(device);
		  
		#  // driver.findElement(By.id("nav-search-submit-button")).click();
		  
		  
# 		  Thread.sleep(1000);
		  
		
# 	}
	
	
# 	    @DataProvider
# 	    public Object[]ratul()
# 	    {
# 	    	return new Object[]
# 	    			{
# 	    		     "Sumsung"
	    		     
	    		
# 	    			};
# 	    }




# import unittest
# import sys

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# #from testingbotclient import TestingBotClient

# class Selenium2TestingBot(unittest.TestCase):

# 	def setUp(self):
# 		desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
# 		desired_capabilities['version'] = 'latest'
# 		desired_capabilities['platform'] = 'WINDOWS'
# 		desired_capabilities['name'] = 'Testing Selenium with Python'

# 		self.driver = webdriver.Remote(
# 			desired_capabilities=desired_capabilities,
# 			command_executor="http://key:secret@hub.testingbot.com/wd/hub"
# 		)
# 		self.driver.implicitly_wait(30)

# 	def test_google(self):
# 		self.driver.get('http://www.google.com')
# 		assert "Google" in self.driver.title

# 	def tearDown(self):
# 		self.driver.quit()
# 		status = sys.exc_info() == (None, None, None)
# 		tb_client = TestingBotClient('key', 'secret')
# 		tb_client.tests.update_test(self.driver.session_id, self._testMethodName, status)

# if __name__ == '__main__':
# 	unittest.main()