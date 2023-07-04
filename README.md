# Microsoft Rewards Points Automation Script
<p>This project contains a Python script that automates Bing searches to accumulate Microsoft Rewards points.</p>

<h3>Description</h3>
<p>The main objective of this project was to streamline and automate the process of accumulating Microsoft Rewards Points, a reward program by Microsoft for using Bing's search engine and other services. This script uses Selenium WebDriver for browser automation to emulate searches on Bing via different browsers (Chrome, Firefox in mobile mode, and Microsoft Edge).
<br/><br/>
Please note that such automation might violate Microsoft Rewards program's terms of service, hence it's advised to use it for educational purposes only.</p>
<h3>Getting Started</h3>
<h4>Dependencies</h4>
<ul>
  <li>Python 3.7 or above</li>
  <li>Selenium WebDriver</li>
  <li>webdriver_manager</li>
  <li>re, requests, json, smtplib, ssl libraries</li>
</ul>
<h4>Installing</h4>
<ol>
  <li>Clone this repository to your local machine.</li>
  <li>Make sure you have Python 3.7 or above installed.</li>
  <li>Install Selenium WebDriver by running <b>'pip install selenium'</b> in your terminal or command prompt.</li>
  <li>Install webdriver_manager by running <b>'pip install webdriver_manager'</b>.</li>
</ol>
<h4>Executing program</h4>
<ol>
  <li>Open <b>'settings.py'</b> and fill in your username, password, SMTP server details, and the URL of Bing's search engine.</li>
  <li>Run <b>'python <script_name>.py'</b> in your terminal.</li>
</ol>
<h4>Functions</h4>
<ul>
  <li><b>'main()'</b>: The main function.</li>
  <li><b>'browser_select(browser)'</b>: Initializes a WebDriver object for the selected browser type.</li>
  <li><b>'fill_form(driver, css_selector, key)'</b>: Fills a form field identified by a CSS selector with a specified key.</li>
  <li><b>'check_login_success(driver)'</b>: Checks whether the login was successful.</li>
  <li><b>'account_login(driver)'</b>: Handles the process of logging into an account.</li>
  <li><b>'get_score(driver)'</b>: Retrieves the current and total score for PC searches, Mobile searches, and Microsoft Edge bonus searches.</li>
  <li><b>'check_scores(driver, pc_searchs_needed, mobile_searchs_needed, edge_searches_needed)'</b>: Checks whether any searches are needed for each category and performs those searches if required.'</b></li>
  <li><b>'searchTermList(num_of_searches)'</b>: Fetches a list of random words to be used for searches.</li>
  <li><b>'perform_search(driver, num_of_searches)'</b>: Carries out the required number of searches using the Bing search engine.</li>
  <li><b>'send_email()'</b>: Sends an email when all searches are completed.</li>
</ul>
<h4>Help</h4>
    If you encounter any issues, please create an issue in this repository.
<h4>Authors</h4>
    <p>ch11nv11n
    <br>
    Your Contact Information
    <ul><li><b>DISCORD</b>: ch11nv11n</li></ul>
    </p>
<h4>Version History</h4>
<ul>
  <li>0.1</li>
  <ul><li>Initial Release</li></ul>
</ul>
<h4>License</h4>
    <p>This project is licensed under the [MIT License] - see the LICENSE.md file for details.</p>
<h4>Acknowledgments</h4>
    <p>Please remember to acknowledge any sources of code or inspiration you used while developing this script.
      <br><br>
      <b>NOTE</b>: This script is primarily intended for educational purposes. It is not advised to use this script to accumulate points on Bing, as it may be against Microsoft's terms of service. Use this script responsibly.</p>
