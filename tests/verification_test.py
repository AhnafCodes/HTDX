from tdom import html

def test_basic_html():
    node = html(t"<div>Hello</div>")
    assert str(node) == "<div>Hello</div>"

def test_attributes():
    node = html(t"<div class='foo' id='bar'></div>")
    assert str(node) == '<div class="foo" id="bar"></div>'

def test_component_snake_case():
    def MyComp(**kwargs):
        # Check what we receive
        return html(t"<div {kwargs} />")

    # Pass a hyphenated attribute
    node = html(t"<{MyComp} data-test='123' />")
    # We expect kwargs to have 'data_test'
    # And when spread back into div, it becomes 'data_test="123"'
    print(f"Result: {node}")
    assert 'data_test="123"' in str(node)

def test_component_explicit_args():
    def Link(*, href: str, **kwargs):
        return html(t"<a href={href} {kwargs} />")

    node = html(t"<{Link} href='/foo' hx-get='/bar' />")
    print(f"Link Result: {node}")
    assert 'href="/foo"' in str(node)
    assert 'hx_get="/bar"' in str(node)

if __name__ == "__main__":
    test_basic_html()
    test_attributes()
    test_component_snake_case()
    test_component_explicit_args()
    print("All tests passed")
