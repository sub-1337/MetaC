#pragma once
#include <spdlog/spdlog.h>
#include <string>
#include <vector>
#include <any>

namespace mc
{
	enum class token_type
	{
		none,
		teminal,
		set,
		colon, // двоеточие
		semicolon, // точка с запятой
		object,

		open_bracket_round,
		close_bracket_round,

		open_braket_square,
		close_braket_square,

		open_braket_qurly,
		close_braket_qurly,

		quotes_single,
		quotes_double
	};
	enum class terminal
	{
		none,
		let
	};
	using str = std::string;
	using num = long long;
	struct token
	{
		token_type type = token_type::none;
		std::any value;
		template<class T>
		void setValue(token_type t, T val)
		{
			type = t,
			value = val;
		}
		template<class T>
		T getValue()
		{
			return std::any_cast<T>(value);
		}
	};
	using token_stream = std::vector<token>;

	class lexer
	{
	public:
		token_stream parse(const std::string& src)
		{
			spdlog::set_level(spdlog::level::debug);
			token_stream out;

			for (int i = 0; i < src.length(); i++) 
			{
				auto it = str(1, src[i]);
				token t;
				t.setValue<str>(token_type::object, it);
				//t.setValue(token_type::object, str(*it));
				out.push_back(t);
				//*it = std::toupper(*it);
			}


			return out;
		}
	};
}
