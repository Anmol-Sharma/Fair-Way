import unittest
from unittest import TestCase
from fair_analysis.splitter import Splitter
import json

# assertEqual, assertTrue : for testing
content_splitter = Splitter()


class TestSplitter(TestCase):
    # TODO: Define the pending tests
    # def test_xml_split(self):
    #     # content_splitter.split_file()
    #     pass

    # def test_html_split(self):
    #     # content_splitter.split_file()
    #     pass

    # def test_markdown_split(self):
    #     # content_splitter.split_file()
    #     pass

    def test_json_split(self):
        sample_json1 = json.dumps(
            {"key1": "value1", "key2": {"nested_key": "nested_value"}},
            separators=(",", ":"),
        )
        sample_json2 = json.dumps(
            {
                "library": {
                    "name": "Central City Library",
                    "location": "123 Main St, Central City",
                    "catalogue": [
                        {
                            "id": "001",
                            "title": "The Great Gatsby",
                            "author": "F. Scott Fitzgerald",
                            "publishedYear": 1925,
                            "genres": ["Novel", "Fiction"],
                            "copies": [
                                {"copyId": "C001", "status": "available"},
                                {"copyId": "C002", "status": "checked_out"},
                            ],
                            "reviews": [
                                {
                                    "reviewer": "Alice Johnson",
                                    "rating": 5,
                                    "comment": "A timeless classic that captures the essence of the Roaring Twenties.",
                                },
                                {
                                    "reviewer": "Bob Smith",
                                    "rating": 4,
                                    "comment": "Great narrative and characters, though a bit slow at times.",
                                },
                            ],
                        },
                        {
                            "id": "002",
                            "title": "1984",
                            "author": "George Orwell",
                            "publishedYear": 1949,
                            "genres": ["Dystopian", "Political Fiction"],
                            "copies": [
                                {"copyId": "C003", "status": "available"},
                                {"copyId": "C004", "status": "checked_out"},
                            ],
                            "reviews": [
                                {
                                    "reviewer": "Carol Lee",
                                    "rating": 5,
                                    "comment": "A chilling and thought-provoking novel that remains relevant today.",
                                },
                                {
                                    "reviewer": "David Kim",
                                    "rating": 4,
                                    "comment": "Intriguing and terrifying, Orwell's vision is eerily prescient.",
                                },
                            ],
                        },
                        {
                            "id": "003",
                            "title": "To Kill a Mockingbird",
                            "author": "Harper Lee",
                            "publishedYear": 1960,
                            "genres": ["Southern Gothic", "Bildungsroman"],
                            "copies": [
                                {"copyId": "C005", "status": "available"},
                                {"copyId": "C006", "status": "checked_out"},
                            ],
                            "reviews": [
                                {
                                    "reviewer": "Eve Brown",
                                    "rating": 5,
                                    "comment": "A powerful exploration of morality and justice.",
                                },
                                {
                                    "reviewer": "Frank Green",
                                    "rating": 4,
                                    "comment": "Compelling narrative with memorable characters.",
                                },
                            ],
                        },
                        {
                            "id": "004",
                            "title": "Pride and Prejudice",
                            "author": "Jane Austen",
                            "publishedYear": 1813,
                            "genres": ["Romance", "Satire"],
                            "copies": [
                                {"copyId": "C007", "status": "available"},
                                {"copyId": "C008", "status": "checked_out"},
                            ],
                            "reviews": [
                                {
                                    "reviewer": "Grace Hall",
                                    "rating": 5,
                                    "comment": "A witty and insightful look at manners and marriage.",
                                },
                                {
                                    "reviewer": "Henry White",
                                    "rating": 4,
                                    "comment": "Engaging characters and a delightful story.",
                                },
                            ],
                        },
                        {
                            "id": "005",
                            "title": "Moby-Dick",
                            "author": "Herman Melville",
                            "publishedYear": 1851,
                            "genres": ["Adventure", "Epic"],
                            "copies": [
                                {"copyId": "C009", "status": "available"},
                                {"copyId": "C010", "status": "checked_out"},
                            ],
                            "reviews": [
                                {
                                    "reviewer": "Ivy Black",
                                    "rating": 4,
                                    "comment": "A monumental tale of obsession and adventure.",
                                },
                                {
                                    "reviewer": "Jack Blue",
                                    "rating": 3,
                                    "comment": "Rich in detail but can be slow-paced.",
                                },
                            ],
                        },
                    ],
                    "members": [
                        {
                            "memberId": "M001",
                            "name": "John Doe",
                            "email": "johndoe@example.com",
                            "borrowedBooks": ["C002", "C004"],
                        },
                        {
                            "memberId": "M002",
                            "name": "Jane Smith",
                            "email": "janesmith@example.com",
                            "borrowedBooks": [],
                        },
                        {
                            "memberId": "M003",
                            "name": "Alice Green",
                            "email": "alicegreen@example.com",
                            "borrowedBooks": ["C006"],
                        },
                        {
                            "memberId": "M004",
                            "name": "Bob Brown",
                            "email": "bobbrown@example.com",
                            "borrowedBooks": ["C008", "C010"],
                        },
                    ],
                }
            },
            separators=(",", ":"),
        )
        chunks1 = content_splitter.split_file(
            file_type="application/json",
            file_size=len(sample_json1),
            file_content=sample_json1,
        )
        self.assertTrue(len(chunks1) == 1, "Length of chunk test-1 does not conform.")
        self.assertEqual(
            json.dumps(
                chunks1[0],
                separators=(",", ":"),
            ),
            """{"key1":"value1","key2":{"nested_key":"nested_value"}}""",
            "Chunk Split for chunk-set-1 does not Conform",
        )
        chunks2 = content_splitter.split_file(
            file_type="application/json",
            file_size=len(sample_json2),
            file_content=sample_json2,
        )
        self.assertTrue(
            len(chunks2) == 2, f"Length of chunk test-2 does not conform:{len(chunks2)}"
        )
        self.assertEqual(
            json.dumps(
                chunks2[1],
                separators=(",", ":"),
            ),
            """{"library":{"members":[{"memberId":"M001","name":"John Doe","email":"johndoe@example.com","borrowedBooks":["C002","C004"]},{"memberId":"M002","name":"Jane Smith","email":"janesmith@example.com","borrowedBooks":[]},{"memberId":"M003","name":"Alice Green","email":"alicegreen@example.com","borrowedBooks":["C006"]},{"memberId":"M004","name":"Bob Brown","email":"bobbrown@example.com","borrowedBooks":["C008","C010"]}]}}""",
            "Chunk Split for chunk-set-2 does not Conform",
        )


if __name__ == "__main__":
    unittest.main()
