"""Unit tests for pipeline/kb.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pipeline"))
import kb

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestKB(unittest.TestCase):
    def test_list_files(self):
        files = kb.list_files(ROOT)
        self.assertGreaterEqual(len(files), 25)
        self.assertTrue(all(f.endswith(".md") for f in files))

    def test_clip_preserve_edges(self):
        text = "HEAD_" + ("X" * 1000) + "_TAIL"
        clipped = kb._clip_preserve_edges(text, 100)
        self.assertLessEqual(len(clipped), 150)
        self.assertTrue(clipped.startswith("HEAD_"))
        self.assertTrue(clipped.endswith("_TAIL"))

    def test_search_and_ranking(self):
        hits = kb.search(ROOT, "悬念", limit=5)
        self.assertGreater(len(hits), 0)
        rel, line_no, content = hits[0]
        self.assertIn("悬念", content)
        self.assertIsInstance(line_no, int)

    def test_project_level_extra_modules(self):
        base = kb.stage_modules("concept", "short")
        self.assertIn("09-短篇写作", base)
        self.assertNotIn("10-题材模块/悬疑推理", base)
        extra = kb.stage_modules("concept", "short", extra=["10-题材模块/悬疑推理"])
        self.assertIn("10-题材模块/悬疑推理", extra)
        self.assertIn("09-短篇写作", extra)
        # 去重
        again = kb.stage_modules("concept", "short",
                                 extra=["09-短篇写作", "10-题材模块/悬疑推理"])
        self.assertEqual(again.count("09-短篇写作"), 1)

    def test_genre_module_auto_mount(self):
        mods = kb.stage_modules("world", "novel", genre="言情")
        self.assertIn("10-题材模块/言情", mods)
        self.assertNotIn("10-题材模块/言情", kb.stage_modules("world", "novel"))

    def test_load_budget_distribution(self):
        # 验证 world 阶段加载不会饿死 02-世界设定
        text = kb.load(ROOT, ["02-世界设定", "04-情节结构"], cap=6000)
        self.assertIn("世界设定", text)
        self.assertIn("情节结构", text)

    def test_retrieve_snippets(self):
        snippets = kb.retrieve_snippets(ROOT, "悬念 伏笔 钩子", cap=2000, max_snippets=2)
        self.assertGreater(len(snippets), 0)
        self.assertIn("参考模块", snippets)


if __name__ == "__main__":
    unittest.main()
