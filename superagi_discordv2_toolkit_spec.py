import unittest
from superagi_discordv2_toolkit import SuperAGI_DiscordV2

class SuperAGIDiscordV2ToolkitSpec(unittest.TestCase):
    def test_authenticate_with_valid_token(self):
        discord_toolkit = SuperAGI_DiscordV2()
        token = "valid_token"
        
        result = discord_toolkit.authenticate(token)
        
        self.assertTrue(result)
    
    def test_authenticate_with_invalid_token(self):
        discord_toolkit = SuperAGI_DiscordV2()
        token = "invalid_token"
        
        with self.assertRaises(ValueError):
            discord_toolkit.authenticate(token)
    
    def test_send_message_with_valid_parameters(self):
        discord_toolkit = SuperAGI_DiscordV2()
        channel_id = "123456789"
        message = "Hello, Discord!"
        image_url = "https://example.com/image.jpg"
        
        result = discord_toolkit.send_message(channel_id, message, image_url)
        
        self.assertTrue(result)
    
    def test_send_message_with_invalid_channel_id(self):
        discord_toolkit = SuperAGI_DiscordV2()
        channel_id = "invalid_channel_id"
        message = "Hello, Discord!"
        image_url = "https://example.com/image.jpg"
        
        with self.assertRaises(ValueError):
            discord_toolkit.send_message(channel_id, message, image_url)
    
    def test_send_message_with_invalid_message(self):
        discord_toolkit = SuperAGI_DiscordV2()
        channel_id = "123456789"
        message = ""
        image_url = "https://example.com/image.jpg"
        
        with self.assertRaises(ValueError):
            discord_toolkit.send_message(channel_id, message, image_url)
    
    def test_send_message_with_invalid_image_url(self):
        discord_toolkit = SuperAGI_DiscordV2()
        channel_id = "123456789"
        message = "Hello, Discord!"
        image_url = "invalid_image_url"
        
        with self.assertRaises(ValueError):
            discord_toolkit.send_message(channel_id, message, image_url)

if __name__ == '__main__':
    unittest.main()
