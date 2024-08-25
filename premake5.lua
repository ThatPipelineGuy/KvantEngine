workspace "KvantEngine"
    configurations { "Debug", "Release" }
    platforms { "Win64", "Linux", "Mac" }
    location "."

    objdir "Build/Intermediate/%{cfg.platform}/%{cfg.buildcfg}"
    targetdir "Build/Binaries/%{cfg.buildcfg}/%{cfg.platform}"

    startproject "Engine"

project "Engine"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"
    location "."

    files {
        "Engine/**.h",
        "Engine/**.cpp",
        "Engine/**.inl",
        "Engine/**.hpp",
        "Engine/KVEngine.cpp",
    }

    includedirs {
        "Engine",
        "Engine/ThirdParty/SDL2-2.0.0/include"
    }

    libdirs {
        "Engine/ThirdParty/SDL2-2.0.0/lib/x64"
    }

    links {
        "SDL2", 
        "SDL2main",
        "legacy_stdio_definitions"  -- Provides __imp___iob_func
    }

    filter "configurations:Debug"
        defines { "DEBUG" }
        symbols "On"
        runtime "Debug"  -- Use Multi-threaded Debug DLL (/MDd)
        linkoptions { "/NODEFAULTLIB:LIBCMT.lib" }  -- Exclude conflicting static C runtime

    filter "configurations:Release"
        defines { "NDEBUG" }
        optimize "On"
        runtime "Release"  -- Use Multi-threaded DLL (/MD)
        linkoptions { "/NODEFAULTLIB:LIBCMT.lib" }  -- Exclude conflicting static C runtime

    filter "platforms:Win64"
        system "Windows"
        architecture "x64"

    filter "platforms:Linux"
        system "Linux"
        architecture "x86_64"

    filter "platforms:Mac"
        system "MacOSX"
        architecture "x86_64"
