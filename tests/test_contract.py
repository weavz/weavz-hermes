import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class HermesContract(unittest.TestCase):
 def test_isolated_profile_commands_and_oauth_url(self):
  readme=(ROOT/"README.md").read_text()
  self.assertIn('HERMES_HOME="$PWD/.local/hermes" hermes mcp add weavz --url https://platform.weavz.io/mcp/weavz --auth oauth',readme)
  self.assertIn('hermes mcp test weavz',readme)
  self.assertIn('browser sign-in',readme)
 def test_instructions_no_secrets(self):
  text=(ROOT/"AGENTS.md").read_text()+(ROOT/".hermes.md").read_text()
  self.assertIn('Do not commit credentials',text)
  self.assertNotIn('wvz_',text); self.assertNotIn('mcp_',text)
if __name__=='__main__': unittest.main()
