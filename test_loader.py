import unittest
import pandas as pd

from loader import (
    build_geo_dataframe,
    fetch_location_data,
    get_geolocator,
)


class TestLoader(unittest.TestCase):

    def test_valid_locations(self):
        # Locations to test
        locations = [
            "Museum of Modern Art",
            "USS Alabama Battleship Memorial Park"
        ]

        # Get location data
        df = build_geo_dataframe(locations)

        # Check that both locations are returned
        self.assertEqual(len(df), 2)

        # Test Museum of Modern Art
        self.assertEqual(
            df.iloc[0]["location"],
            "Museum of Modern Art"
        )
        self.assertAlmostEqual(
            df.iloc[0]["latitude"], 40.7618552, delta=0.01
        )
        self.assertAlmostEqual(
            df.iloc[0]["longitude"], -73.9782438, delta=0.01
        )
        self.assertEqual(
            str(df.iloc[0]["type"]).lower(), "museum"
        )

        # Test USS Alabama Battleship Memorial Park
        self.assertEqual(
            df.iloc[1]["location"],
            "USS Alabama Battleship Memorial Park"
        )
        self.assertAlmostEqual(
            df.iloc[1]["latitude"], 30.684373, delta=0.01
        )
        self.assertAlmostEqual(
            df.iloc[1]["longitude"], -88.015316, delta=0.01
        )
        self.assertEqual(
            str(df.iloc[1]["type"]).lower(), "park"
        )

    def test_invalid_location(self):
        # Test a nonexistent location
        geolocator = get_geolocator()
        result = fetch_location_data(
            geolocator, "asdfqwer1234"
        )

        # Check the location name
        self.assertEqual(
            result["location"], "asdfqwer1234"
        )

        # Check missing values
        self.assertTrue(pd.isna(result["latitude"]))
        self.assertTrue(pd.isna(result["longitude"]))
        self.assertTrue(pd.isna(result["type"]))


if __name__ == "__main__":
    unittest.main()