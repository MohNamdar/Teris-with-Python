def playground(playground):
    width = 16
    res = ['┌' + '─' * width + '┐']
    for s in playground:
        res.append('│' + (''.join(s) + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)
