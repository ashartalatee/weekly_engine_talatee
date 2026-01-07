from parser import parse_html

SAMPLE_HTML = """
<html>
  <body>
    <div class="item">
      <h2>Product A</h2>
      <span class="price">100</span>
    </div>
    <div class="item">
      <h2>Product B</h2>
      <span class="price">200</span>
    </div>
  </body>
</html>
"""

def test_parse_html_basic():
    selectors = {
        "container": "div.item",
        "fields": {
            "name": "h2",
            "price": "span.price"
        }
    }

    data = parse_html(SAMPLE_HTML, selectors)

    assert len(data) == 2
    assert data[0]["name"] == "Product A"
    assert data[1]["price"] == "200"
