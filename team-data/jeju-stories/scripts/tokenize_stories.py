#!/usr/bin/env python3
"""
Jeju Folklore Tokenization Script
Converts raw story JSON files into tokenized training data for controlled generation
"""

import json
import re
import os
from typing import Dict, List, Any
from pathlib import Path

class JejuFolkloreTokenizer:
    def __init__(self):
        self.token_definitions = self.load_token_definitions()
        
    def load_token_definitions(self) -> Dict:
        """Load predefined token categories and mappings"""
        return {
            "characters": {
                "설문대할망": "[CHR:Seolmundae:Goddess]",
                "할아버지": "[CHR:Elder:Male]", 
                "할머니": "[CHR:Elder:Female]",
                "아이": "[CHR:Child:Curious]",
                "용": "[CHR:Spirit:Dragon]",
                "신": "[CHR:Spirit:Divine]"
            },
            "locations": {
                "한라산": "[LOC:Hallasan:Sacred]",
                "성산일출봉": "[LOC:SS-A1:Seongsan]",
                "바다": "[LOC:Coast:Ocean]",
                "마을": "[LOC:Village:Traditional]",
                "숲": "[LOC:Forest:Mysterious]",
                "오름": "[LOC:Oreum:Volcanic]"
            },
            "plot_elements": {
                "창조": "[PLOT:Origin]",
                "변신": "[PLOT:Transformation]",
                "여행": "[PLOT:Quest]", 
                "교훈": "[PLOT:Moral]",
                "갈등": "[PLOT:Conflict]"
            },
            "styles": {
                "simple": "[STYLE:Child:3-5]",
                "educational": "[STYLE:Child:6-10]",
                "traditional": "[STYLE:Elder:Traditional]",
                "formal": "[STYLE:Academic:Formal]",
                "casual": "[STYLE:Modern:Casual]"
            }
        }
    
    def extract_story_elements(self, story_json: Dict) -> Dict:
        """Extract tokenizable elements from a story JSON"""
        elements = {
            "characters": [],
            "locations": [],
            "plot_points": [],
            "cultural_markers": []
        }
        
        # Extract content text for analysis
        content_text = ""
        if "content" in story_json:
            if "summary" in story_json["content"]:
                content_text += story_json["content"]["summary"] + " "
            
            if "episodes" in story_json["content"]:
                for episode in story_json["content"]["episodes"]:
                    if "content" in episode:
                        content_text += episode["content"] + " "
        
        # Character detection
        for char_name, token in self.token_definitions["characters"].items():
            if char_name in content_text:
                elements["characters"].append(token)
        
        # Location detection  
        for loc_name, token in self.token_definitions["locations"].items():
            if loc_name in content_text:
                elements["locations"].append(token)
                
        # Plot element detection
        for plot_keyword, token in self.token_definitions["plot_elements"].items():
            if plot_keyword in content_text:
                elements["plot_points"].append(token)
        
        # Cultural markers
        if "cultural_significance" in story_json.get("content", {}):
            elements["cultural_markers"] = story_json["content"]["cultural_significance"]
        
        return elements
    
    def generate_tokenized_prompt(self, elements: Dict, target_style: str = "traditional") -> str:
        """Generate a tokenized prompt from extracted elements"""
        prompt_parts = []
        
        # Add style token
        if target_style in self.token_definitions["styles"]:
            prompt_parts.append(self.token_definitions["styles"][target_style])
        
        # Add character tokens
        if elements["characters"]:
            prompt_parts.extend(elements["characters"][:2])  # Limit to 2 main characters
            
        # Add location tokens  
        if elements["locations"]:
            prompt_parts.append(elements["locations"][0])  # Primary location
            
        # Add plot tokens
        if elements["plot_points"]:
            prompt_parts.append(elements["plot_points"][0])  # Main plot type
            
        prompt_parts.append("[GENERATE_STORY]")
        
        return " ".join(prompt_parts)
    
    def rewrite_for_style(self, original_text: str, target_style: str) -> str:
        """Rewrite story content for different target audiences"""
        
        if target_style == "[STYLE:Child:3-5]":
            # Simplify language for preschoolers
            simplified = self.simplify_language(original_text)
            return self.add_child_friendly_elements(simplified)
            
        elif target_style == "[STYLE:Child:6-10]":
            # Educational version for elementary age
            return self.add_educational_elements(original_text)
            
        elif target_style == "[STYLE:Elder:Traditional]":
            # Traditional storytelling format
            return self.add_traditional_storytelling_markers(original_text)
            
        elif target_style == "[STYLE:Academic:Formal]":
            # Formal, scholarly tone
            return self.add_formal_academic_tone(original_text)
            
        else:
            return original_text
    
    def simplify_language(self, text: str) -> str:
        """Convert complex text to child-friendly language"""
        # Replace complex words with simpler alternatives
        replacements = {
            "설문대할망": "아주 큰 할머니",
            "창조했다": "만들었어요",
            "형성했다": "만들어졌어요", 
            "거대한": "아주 큰",
            "신비로운": "신기한"
        }
        
        result = text
        for complex_word, simple_word in replacements.items():
            result = result.replace(complex_word, simple_word)
            
        return result
    
    def add_child_friendly_elements(self, text: str) -> str:
        """Add engaging elements for young children"""
        # Add excitement and direct address
        text = "옛날에 " + text
        text = text.replace(".", "요!")
        text = text.replace("했다", "했답니다")
        return text + " 정말 멋진 이야기죠?"
    
    def add_educational_elements(self, text: str) -> str:
        """Add educational elements for elementary age children"""
        # Add questions and learning prompts
        text = "알고 있니? " + text
        text = text.replace(".", "이에요.")
        text = text.replace("했다", "했어요")
        return text + " 어떻게 생각해?"
    
    def add_traditional_storytelling_markers(self, text: str) -> str:
        """Add traditional Korean storytelling elements"""
        # Use formal storytelling language
        text = "옛적에 " + text
        text = text.replace("했다", "했습니다")
        text = text.replace("이다", "입니다")
        return text
    
    def add_formal_academic_tone(self, text: str) -> str:
        """Convert to formal academic writing style"""
        # Use scholarly language
        text = text.replace("했다", "한 것으로 전승됩니다")
        text = text.replace("이다", "로 여겨집니다")
        text = text.replace("말했다", "기술되어 있습니다")
        return text
    
    def generate_training_sample(self, story_json: Dict, target_style: str) -> Dict:
        """Generate a complete training sample from a story"""
        
        # Extract story elements
        elements = self.extract_story_elements(story_json)
        
        # Generate tokenized prompt
        prompt = self.generate_tokenized_prompt(elements, target_style)
        
        # Get base content
        base_content = ""
        if "content" in story_json and "summary" in story_json["content"]:
            base_content = story_json["content"]["summary"]
        
        # Rewrite for target style
        styled_content = self.rewrite_for_style(base_content, self.token_definitions["styles"][target_style])
        
        return {
            "id": f"{story_json.get('id', 'unknown')}_{target_style}",
            "prompt": prompt,
            "response": styled_content,
            "metadata": {
                "source_story": story_json.get("id", "unknown"),
                "target_style": target_style,
                "extracted_elements": elements,
                "cultural_context": story_json.get("content", {}).get("cultural_significance", []),
                "complexity_score": self.calculate_complexity_score(styled_content)
            }
        }
    
    def calculate_complexity_score(self, text: str) -> int:
        """Calculate text complexity for training weighting"""
        # Simple heuristic based on sentence length and vocabulary
        sentences = text.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
        
        if avg_sentence_length < 8:
            return 1  # Simple
        elif avg_sentence_length < 15:
            return 2  # Medium
        else:
            return 3  # Complex
    
    def process_story_file(self, story_file_path: str) -> List[Dict]:
        """Process a single story JSON file and generate training variations"""
        
        with open(story_file_path, 'r', encoding='utf-8') as f:
            story_json = json.load(f)
        
        training_samples = []
        
        # Generate samples for different styles
        styles = ["simple", "educational", "traditional", "formal"]
        
        for style in styles:
            sample = self.generate_training_sample(story_json, style)
            training_samples.append(sample)
        
        return training_samples
    
    def process_all_stories(self, input_dir: str, output_dir: str):
        """Process all story files in a directory"""
        
        input_path = Path(input_dir)
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        all_training_data = []
        
        # Process each JSON file
        for json_file in input_path.glob("*.json"):
            print(f"Processing {json_file.name}...")
            
            try:
                training_samples = self.process_story_file(str(json_file))
                all_training_data.extend(training_samples)
                
            except Exception as e:
                print(f"Error processing {json_file.name}: {e}")
                continue
        
        # Save consolidated training data
        output_file = output_path / "jeju_folklore_training_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "metadata": {
                    "total_samples": len(all_training_data),
                    "source_stories": len(list(input_path.glob("*.json"))),
                    "generation_date": "2025-12-03",
                    "token_system_version": "1.0"
                },
                "training_samples": all_training_data
            }, f, ensure_ascii=False, indent=2)
        
        print(f"Generated {len(all_training_data)} training samples")
        print(f"Saved to {output_file}")
        
        # Generate summary statistics
        self.generate_statistics_report(all_training_data, output_path)
    
    def generate_statistics_report(self, training_data: List[Dict], output_dir: Path):
        """Generate a report on the training data characteristics"""
        
        stats = {
            "total_samples": len(training_data),
            "style_distribution": {},
            "complexity_distribution": {},
            "character_frequency": {},
            "location_frequency": {}
        }
        
        for sample in training_data:
            # Style distribution
            style = sample["metadata"]["target_style"]
            stats["style_distribution"][style] = stats["style_distribution"].get(style, 0) + 1
            
            # Complexity distribution
            complexity = sample["metadata"]["complexity_score"]
            stats["complexity_distribution"][complexity] = stats["complexity_distribution"].get(complexity, 0) + 1
        
        # Save statistics report
        stats_file = output_dir / "training_statistics.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        print(f"Statistics report saved to {stats_file}")

if __name__ == "__main__":
    # Initialize tokenizer
    tokenizer = JejuFolkloreTokenizer()
    
    # Process stories from cleaned directory
    input_directory = "../cleaned/stories/myths/"
    output_directory = "./training_data/"
    
    # Check if input directory exists
    if not os.path.exists(input_directory):
        print(f"Input directory not found: {input_directory}")
        print("Available directories:")
        parent_dir = "../"
        if os.path.exists(parent_dir):
            for item in os.listdir(parent_dir):
                if os.path.isdir(os.path.join(parent_dir, item)):
                    print(f"  - {item}/")
        exit(1)
    
    print("Starting Jeju Folklore tokenization process...")
    tokenizer.process_all_stories(input_directory, output_directory)
    print("Tokenization complete!")