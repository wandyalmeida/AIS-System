<h1 align="center"> AIS-System: Automated File Download and Conversion Application </h1>

##

## ✔️ Overview

<p>
  The AIS-System (Automated File Download and Conversion Application) is a project designed to streamline the daily task of downloading a specific file from the JMC website and converting it to a modified format. The application automates the login process, filters the desired time range, searches for the file, downloads it, and converts it from HTML to XLSX format.
</p>

## 

## 🔨 Tools used 
  <div style="display: inline_block"><br>
  <img align="center" alt="wandy-Py" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
</div>

##

## ✔️ Features:

<ul>
  <li><b>Automated Login:</b> The application automatically logs in to the JMC website, eliminating the need for manual login by the employee.</li>
  <li><b>Date Filtering:</b> The application filters the files based on a specified time range of 7 days, ensuring that only the relevant files are downloaded.</li>
  <li><b>File Search:</b> The application searches for the desired file within the filtered results, saving time and effort for the employee.</li>
  <li><b>Download and Storage:</b> Before initiating the download, the application checks if the company's system has a folder named "Temp." If the folder doesn't exist, it creates it. Additionally, the application creates a folder named "AIS" within the "Temp" folder. The downloaded file is then saved in the "AIS" folder for further processing.</li>
  <li><b>File Conversion:</b> After the download, the application converts the downloaded file from HTML format to XLSX format. This conversion enables easier modification and processing of the file.</li>
</ul>

##

## ✔️ Setup Instructions

<ol>
  <li><b>Prerequisites:</b> Ensure that the following dependencies are installed on the system:
    <ul>
      <li>Internet connectivity</li>
      <li>Web browser (Google Chrome, Mozilla Firefox, or Microsoft Edge)</li>
      <li>Python (version 3.7 or higher)</li>
    </ul>
  </li>
  <li>
    <b>Installation:</b>
    <ul>
    <li>Clone or download the project repository from GitHub.</li>
    </ul>
  </li>
  <li>
    <b>Configuration:</b>
    <ul>
      <li>Open the main.py file in a text editor.</li>
      <li>Provide the necessary login credentials for the JMC website in the username and password fields.</li>
      <li>Configure any other desired settings in the configuration file, such as file paths or download preferences.</li>
    </ul>
  </li>
  <li>
    <b>Execution:</b>
    <ul>
      <li>Open a terminal or command prompt.</li>
      <li>Navigate to the project directory.</li>
      <li>Run the following command to start the application:
        python main.py
      </li>
    </ul>
  </li>
  
  <li>
    <b>Usage:</b>
    <ul>
      <li>The application will automatically launch the web browser and perform the necessary steps to log in to the JMC website.</li>
      <li>After logging in, it will filter the files based on the specified time range.</li>
      <li>The application will then search for the desired file within the filtered results and initiate the download.</li>
      <li>If the "Temp" folder doesn't exist in the system, the application will create it along with the "AIS" folder.</li>
      <li>The downloaded file will be saved in the "AIS" folder.</li>
      <li>Finally, the application will convert the downloaded file from HTML to XLSX format, making it ready for modification.</li>
    </ul>
  </li>
</ol>

##

## ✔️ Libraries Used

<ul>
  <li><b>Selenium:</b> A Python library used for automating web browser interactions. It provides a convenient way to control and interact with web elements, navigate pages, and perform actions such as clicking buttons and filling forms. For more information, refer to the Selenium documentation.</li>
</ul>

##

## ✔️ Disclaimer

<p>Please note that the AIS-System is provided as-is and may require modifications to suit your specific environment or requirements. Use the application responsibly and ensure compliance with any applicable terms of service or legal agreements when interacting with external websites.</p>

##

## ✔️ License

<p>This project is licensed under the MIT License. Feel free to modify and distribute it as needed.</p>

##

## ✔️ Support

<p>For any questions, issues, or suggestions regarding the AIS-System (Automated File Download and Conversion Application), please contact wandwilson.almeida@hotmail.com. We appreciate your feedback and are happy to assist you.</p>



    
  
          
