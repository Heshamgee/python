import yaml
import json
import os

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from YAML file"""
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def update_config(self, key, value):
        """Update configuration value"""
        keys = key.split('.')
        config_ref = self.config
        
        for k in keys[:-1]:
            config_ref = config_ref.setdefault(k, {})
        
        config_ref[keys[-1]] = value
        self.save_config()
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_path, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False)
    
    def validate_config(self):
        """Validate configuration structure"""
        required_fields = ['database', 'api', 'logging']
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field: {field}")
        
        return True
    
    def generate_env_file(self, output_path='.env'):
        """Generate .env file from configuration"""
        env_vars = []
        
        def flatten_dict(d, parent_key=''):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}_{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key).items())
                else:
                    items.append((new_key.upper(), str(v)))
            return dict(items)
        
        flat_config = flatten_dict(self.config)
        
        with open(output_path, 'w') as file:
            for key, value in flat_config.items():
                file.write(f"{key}={value}\n")

# Usage
config_manager = ConfigManager('config.yaml')
config_manager.update_config('database.host', 'localhost')
config_manager.generate_env_file()
