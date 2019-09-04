# XPath:
   ## 选择节点:XPath使用路径表达式来选择XML文档中的节点。通过遵循一个或多个路径来选择节点。
   - /(从根节点中选择)
   - //(从当前节点中选择与选择匹配的文档中的节点，无论它们在何处)
   - .(选择当前节点)
   - ..(选择当前节点的父节点)
   - @(选择属性)
   ## 选择未知节点:XPath通配符可用于选择未知的XML节点
   - *(匹配任何元素节点)
   - @*(匹配任何属性节点)
   - node()(匹配任何类型的任何节点)
   ## 选取多个路径:通过使用 | 在XPath表达式中，您可以选择多个路径
   ## XPath Axes:轴表示与上下文（当前）节点的关系，用于定位与树上该节点相关的节点。
   - ancestor 选择当前节点的所有祖先（父级，祖父级等）
   - ancestor-or-self 选择当前节点和当前节点本身的所有祖先（父级，祖父级等）
   - attribute 选择当前节点的所有属性
   - child 选择当前节点的所有子节点
   - descendant 选择当前节点的所有后代（子节点，孙子节点等）
   - descendant-or-self 选择当前节点和当前节点本身的所有后代（子节点，孙子节点等）
   - following 在当前节点的结束标记之后选择文档中的所有内容
   - following-sibling 选择当前节点之后的所有兄弟节点
   - namespace 选择当前节点的所有命名空间节点
   - parent 选择当前节点的父节点
   - previous 选择文档中当前节点之前出现的所有节点，祖先，属性节点和命名空间节点除外
   - preceding-sibling 选择当前节点之前的所有兄弟节点
   - self 选择当前节点选择当前节点的所有祖先（父级，祖父级等）
   ### Example
   - child :: book 选择作为当前节点的子节点的所有书节点
   - attribute :: lang 选择当前节点的lang属性
   - child :: * 选择当前节点的所有元素子节点
   - attribute :: * 选择当前节点的所有属性
   - child :: text() 选择当前节点的所有文本节点子节点
   - child :: node() 选择当前节点的所有子节点
   - descendant :: book 选择当前节点的所有书籍后代
   - ancestor :: book 选择当前节点的所有书籍祖先
   - ancestor-or-self :: book 选择当前节点的所有书籍祖先 - 以及当前节点的当前节点
   - child :: * / child :: price 选择当前节点的所有价格孙子
   ## 位置路径表达:位置路径可以是绝对路径或相对路径,绝对位置路径以斜杠（/）开头，相对位置路径不是。在这两种情况下，位置路径都包含一个或多个步骤，每个步骤用斜杠分隔：
   - An absolute location path:  /step/step/...
   - A relative location path:   step/step/...
   ## XPath运算符:XPath表达式返回节点集，字符串，布尔值或数字。
   - | 计算两个节点集 //book | //cd
   - (括号无意义) + 加 6 + 4
   - (括号无意义) - 减法 6 - 4
   - (括号无意义) * 乘法 6 * 4
   - div 部 8 div 4
   - = 等于 price=9.80
   - != 不等	 price!=9.80
   - < 低于 price<9.80
   - <= 小于或等于 price<=9.80
   - (括号无意义) > 大于 price>9.80
   - (括号无意义) >= 大于或等于 price>=9.80
   - or 或者 price=9.80 or price=9.70
   - and 和 price>9.00 and price<9.90
   - mod 模数 (除法余数) 5 mod 2