import unittest2 as unittest
from ipynb.fs.full.index import build_trace, layout, trace_values

class TestPlotly(unittest.TestCase):
    def test_build_trace_returns_dict_with_keys_of_x_and_y(self):
        figurekeys = build_trace([]).keys()
        self.assertEqual(list(figurekeys)[0], 'x')
        self.assertEqual(list(figurekeys)[1], 'y')

    def test_build_trace_sets_x_values_as_value_and_y_values_as_value(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = build_trace(data)
        self.assertEqual(test_trace['x'], [1, 3, 2])
        self.assertEqual(test_trace['y'], [1, 2, 5])

    def test_build_trace_takes_second_argument_as_mode_set_to_value_of_mode_key(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = build_trace(data, 'markers')
        self.assertEqual(test_trace['mode'], 'markers')

    def test_build_trace_mode_is_set_to_markers_by_default(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = build_trace(data)
        self.assertEqual(test_trace['mode'], 'markers')

    def test_build_trace_accepts_argument_of_name_set_to_default_argument_of_data(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = build_trace(data)
        self.assertEqual(test_trace['name'], 'data')

    def test_trace_values(self):
        test_trace = trace_values([1, 2, 3], [2, 4, 5], 'line', 'line trace')
        self.assertEqual(test_trace, {'mode': 'line', 'name': 'line trace', 'x': [1, 2, 3], 'y': [2, 4, 5]})

    def test_layout_returns_dictionary(self):
        self.assertTrue(isinstance(layout(), dict))

    def test_layout_returns_dictionary(self):
        self.assertTrue(isinstance(layout(), dict))

    def test_layout_adds_x_axis(self):
        self.assertTrue(layout([1, 5], {'xaxis': {'range': [1, 5]}}))

    def test_layout_adds_y_axis(self):
        self.assertTrue(layout(y_range = [2, 5]), {'yaxis': {'range': [2, 5]}})

    def test_layout_adds_x_axis_and_y_axis(self):
        self.assertTrue(layout(y_range = [2, 5], x_range = [3, 6]), {'yaxis': {'range': [2, 5]}, 'xaxis': {'range': [3, 6]}})

    def test_layout_adds_an_options_argument(self):
        self.assertTrue(layout(y_range = [2, 5]), {'yaxis': {'range': [2, 5]}, 'title': 'sample title'})
