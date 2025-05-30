def read_segments(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        segments = []
        for line in lines[1:]:
            x, y = map(int, line.strip().split())
            segments.append((min(x, y), max(x, y)))
    return segments

def count_min_point(segments):
    segments = sorted(segments, key=lambda x: x[1])
    current_point = None
    counter = 0
    for seg in segments:
        if current_point is None or not (seg[0] <= current_point <= seg[1]):
            current_point = seg[1]
            counter= counter+1
        
    return counter

segments = read_segments('data_prog_contest_problem_1.txt')
print(count_min_point(segments))
