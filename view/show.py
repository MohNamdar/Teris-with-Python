def playground(playground):
    width = len(playground[0])
    res = ['┌' + '─' * width + '┐']
    for r in playground:
        res.append('│' + (''.join(r) + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)
