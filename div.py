from bs4 import BeautifulSoup

# 假设您已经有了一个HTML页面的字符串变量html，可以通过requests库等方式获取
soup = BeautifulSoup(html, 'html.parser')

# 获取select元素
select_element = soup.select_one('select')

# 获取select元素中所有的option元素
option_elements = select_element.select('option')

# 获取最后一个option元素
last_option_element = option_elements[-1]

# 获取最后一个option元素的值（即option标签的value属性值）
last_option_value = last_option_element['value']
