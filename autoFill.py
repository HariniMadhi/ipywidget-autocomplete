import ipywidgets as widgets
def autoFill(options = [''], val = '', txt = '', placehold = '', callback = False):
    
    options.append('')
    def dropFunc(value):
        if (value.new in options):
            dropClose()
            if (callable(callback)):
                callback(value)
        text.value = value.new
        
    def dropClose():
        drop.layout.visibility = 'hidden'
        selDropBox.layout.visibility = 'hidden'            
        selDropBox.layout.display = 'none'
        
    def dropOpen():
        drop.layout.visibility = 'visible'
        selDropBox.layout.visibility = 'visible'
        selDropBox.layout.display = 'flex'
            
    def textFunc(value):
        matched = False
        word = value.new
        if not word:
            drop.options = options
            drop.value = ''
            dropOpen()
            return
        out = [word]
        for option in options:
            if word.lower() in option.lower(): 
                if (option.lower() == word.lower()):
                    matched = True
                out.append(option)
        if (not matched):
            dropOpen()
            out.append('')
            drop.options = out
        else:
            dropClose()
        
    drop = widgets.Select(options = options, value = val, rows = 10, description = txt)
    text = widgets.Text(value = val, placeholder = placehold, description = txt)
    drop.observe(dropFunc, names = 'value')
    text.observe(textFunc, names = 'value')
    
    selTextBox = widgets.Box([text])
    selDropBox = widgets.Box([drop])
    return (widgets.VBox([selTextBox, selDropBox], layout = widgets.Layout(display='flex', flex_flow='column')))


def open(value):
    show.value = value.new
    
options = ['Football', 'Basketball', 'Volleyball', 'Basketcase', 'Showcase', 'Footer', 'Header', 'Viewer', 'Footage', 'Showtime', 'Show Business']

au = autoFill(options, callback = open)
display(au)
