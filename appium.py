from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

# Configuraciones
desired_caps = {
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "app": "/path/to/app.apk"
}

# Crear el driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Localizar elementos
boton_login = driver.find_element(AppiumBy.ID, "com.example.app:id/login_button")
campo_usuario = driver.find_element(AppiumBy.ID, "com.example.app:id/username_field")
campo_contrasena = driver.find_element(AppiumBy.ID, "com.example.app:id/password_field")

# Interactuar con la app
campo_usuario.send_keys("usuario")
campo_contrasena.send_keys("contrasena")
boton_login.click()

# Acciones más complejas
# Ejemplo: Deslizar hacia arriba
action = TouchAction(driver)
action.long_press(x=100, y=100).move_to(x=100, y=500).release().perform()

# Cerrar la app
driver.quit()
