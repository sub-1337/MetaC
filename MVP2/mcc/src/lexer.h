#pragma once
#include <spdlog/spdlog.h>
#include <string>

namespace mc
{
	enum class token_type
	{
		teminal,
		object,

		open_bracket_round,
		close_bracket_round,

		open_braket_square,
		close_braket_square,

		open_braket_qurly,
		close_braket_qurly
	};
	class token
	{

	};
	class lexer
	{
	public:
		void parse(const std::string& src)
		{

		}
	};
}
