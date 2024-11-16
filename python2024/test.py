def g(data, batch_size):
    buffer = []
    total_samples = len(data) * 4
    d = 0  
    for b in data:
        buffer.extend([
            b,
            b[::-1],
            b[len(b)//2:] + b[:len(b)//2],
            b[1:len(b)-1]
        ])
        
        while len(buffer) >= batch_size:
            yield tuple(buffer[:batch_size])
            buffer = buffer[batch_size:]
            d += batch_size
            if d >= total_samples:
                return  
    if buffer:
        while len(buffer) < batch_size:
            for b in data:
                if len(buffer) < batch_size:
                    buffer.extend([
                        b,
                        b[::-1],
                        b[len(b)//2:] + b[:len(b)//2],
                        b[1:len(b)-1]
                    ])
        yield tuple(buffer[:batch_size])