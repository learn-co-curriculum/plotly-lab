import unittest2 as unittest
from ipynb.fs.full.index import build_figure, trace, build_layout

class TestDistance(unittest.TestCase):
    def test_build_figure_returns_dict(self):
        self.assertTrue(isinstance(build_figure(), dict))

    def test_build_figure_takes_arguments_of_traces_and_layout(self):
        self.assertTrue(isinstance(build_figure([], {}), dict))

    def test_build_figure_takes_arguments_of_traces_and_layout(self):
        self.assertTrue(isinstance(build_figure([], {}), dict))

    def test_build_figure_returns_a_dictionary_with_keys_of_data_and_layout(self):
        figurekeys = build_figure([], {}).keys()
        list_keys = list(figurekeys)
        self.assertEqual(list_keys[0], 'data')
        self.assertTrue(list_keys[1], 'layout')

    def test_build_figure_assigns_the_arguments_of_traces_as_the_value_to_the_data(self):
        figure = build_figure(['foobar'], {})
        self.assertEqual(figure['data'], ['foobar'])

    def test_build_figure_assigns_the_arguments_of_layout_as_the_value_to_the_layout(self):
        figure = build_figure(['foobar'], {'title': 'sample title'})
        self.assertEqual(figure['layout'], {'title': 'sample title'})

    def test_sets_a_default_argument_of_an_array_set_to_traces_argument(self):
        figure = build_figure()
        self.assertEqual(figure['data'], [])

    def test_sets_a_default_argument_of_a_dict_set_to_layout_argument(self):
        figure = build_figure()
        self.assertEqual(figure['layout'], {})

    def test_trace_returns_dict_with_keys_of_x_and_y(self):
        figurekeys = trace([]).keys()
        self.assertEqual(list(figurekeys)[0], 'x')
        self.assertEqual(list(figurekeys)[1], 'y')

    def test_trace_sets_x_values_as_value_and_y_values_as_value(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = trace(data)
        self.assertEqual(test_trace['x'], [1, 3, 2])
        self.assertEqual(test_trace['y'], [1, 2, 5])

    def test_trace_takes_second_argument_as_mode_set_to_value_of_mode_key(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = trace(data, 'foobar')
        self.assertEqual(test_trace['mode'], 'foobar')

    def test_trace_mode_is_set_to_markers_by_default(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = trace(data)
        self.assertEqual(test_trace['mode'], 'markers')

    def test_trace_accepts_argument_of_name_set_to_default_argument_of_data(self):
        data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
        test_trace = trace(data)
        self.assertEqual(test_trace['name'], 'data')

    def test_layout_returns_dictionary(self):
        self.assertTrue(isinstance(build_layout(), dict))

    def test_layout_returns_dictionary(self):
        self.assertTrue(isinstance(build_layout(), dict))

    def test_layout_adds_x_axis(self):
        self.assertTrue(build_layout([1, 5], {'xaxis': {'range': [1, 5]}}))

    def test_layout_adds_y_axis(self):
        self.assertTrue(build_layout(y_range = [2, 5]), {'yaxis': {'range': [2, 5]}})

    def test_layout_adds_x_axis_and_y_axis(self):
        self.assertTrue(build_layout(y_range = [2, 5], x_range = [3, 6]), {'yaxis': {'range': [2, 5]}, 'xaxis': {'range': [3, 6]}})

    def test_layout_adds_an_options_argument(self):
        self.assertTrue(build_layout(y_range = [2, 5]), {'yaxis': {'range': [2, 5]}, 'title': 'sample title'})
