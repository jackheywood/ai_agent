def render(expression, result):
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)

    box_width = max(len(expression), len(result_str)) + 4

    box = []

    box.append(get_start_line(box_width))
    box.append(get_content_line(expression, box_width))
    box.append(get_empty_line(box_width))
    box.append(get_equals_line(box_width))
    box.append(get_empty_line(box_width))
    box.append(get_content_line(result_str, box_width))
    box.append(get_end_line(box_width))

    return "\n".join(box)


def get_start_line(box_width):
    return "┌" + "─" * box_width + "┐"


def get_content_line(text, box_width):
    return (
        "│" +
        " " * 2 +
        text +
        " " * (box_width - len(text) - 2)
        + "│"
    )


def get_empty_line(box_width):
    return "│" + " " * box_width + "│"


def get_equals_line(box_width):
    return "│" + " " * 2 + "=" + " " * (box_width - 3) + "│"


def get_end_line(box_width):
    return "└" + "─" * box_width + "┘"
